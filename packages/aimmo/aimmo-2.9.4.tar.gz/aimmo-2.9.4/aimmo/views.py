import logging
import re
from typing import Tuple

from common.models import UserProfile
from common.permissions import CanDeleteGame
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import Http404, HttpResponse, HttpResponseForbidden, JsonResponse, HttpResponseBadRequest
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import mixins, status, viewsets
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
    action,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from . import game_renderer
from .avatar_creator import create_avatar_for_user
from .exceptions import UserCannotPlayGameException
from .models import Avatar, Game
from .permissions import (
    CanDeleteGameOrReadOnly,
    CsrfExemptSessionAuthentication,
    GameHasToken,
)
from .serializers import GameSerializer, GameIdsSerializer

LOGGER = logging.getLogger(__name__)


@login_required
def code(request, id):
    if not request.user:
        LOGGER.info("This request doesn't have a user attached to it.")
        return HttpResponseForbidden()
    game = get_object_or_404(Game, id=id)

    if not game.can_user_play(request.user):
        LOGGER.info("The user doesn't have access to the requested game.")
        raise Http404

    try:
        avatar = game.avatar_set.get(owner=request.user)
    except Avatar.DoesNotExist:
        avatar = create_avatar_for_user(request.user, id)

    if request.method == "POST":
        avatar.code = request.POST["code"]
        avatar.save()
        return HttpResponse()
    else:
        return JsonResponse({"code": avatar.code, "starterCode": game.worksheet.starter_code})


@login_required
def badges(request, id):
    if not request.user:
        LOGGER.info("This request doesn't have a user attached to it.")
        return HttpResponseForbidden()
    game = get_object_or_404(Game, id=id)

    if not game.can_user_play(request.user):
        LOGGER.info("The user doesn't have access to the requested game.")
        raise Http404

    try:
        avatar = game.avatar_set.get(owner=request.user)
    except Avatar.DoesNotExist:
        avatar = create_avatar_for_user(request.user, id)
    avatar_user_profile = UserProfile.objects.get(user=avatar.owner)

    if request.method == "POST":
        earned_badges = request.POST["badges"]

        if re.match("^([1-9]:\d+,)*$", earned_badges):
            avatar_user_profile.aimmo_badges = earned_badges
            avatar_user_profile.save()
            return HttpResponse()
        else:
            LOGGER.info(f"Badges information {earned_badges} doesn't match the required format.")
            return HttpResponseBadRequest()

    else:
        # Making the badges an empty string if the user doesn't have any badges yet
        return JsonResponse({"badges": avatar_user_profile.aimmo_badges or ""})


class GameUsersView(APIView):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = (GameHasToken,)

    def get(self, request, id):
        game = get_object_or_404(Game, id=id)
        data = self.serialize_users(game)
        return JsonResponse(data)

    def serialize_users(self, game):
        users = {"main_avatar": None, "users": []}
        for avatar in game.avatar_set.all():
            if avatar.owner_id == game.main_user_id:
                users["main_avatar"] = avatar.id
            users["users"].append({"id": avatar.id, "code": avatar.code})
        return users


class GameViewSet(
    viewsets.GenericViewSet,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
):
    authentication_classes = (CsrfExemptSessionAuthentication, SessionAuthentication)
    queryset = Game.objects.all()
    permission_classes = (CanDeleteGameOrReadOnly,)
    serializer_class = GameSerializer

    def list(self, request):
        response = {}
        for game in Game.objects.filter(is_archived=False):
            serializer = GameSerializer(game)
            response[game.pk] = serializer.data
        return Response(response)

    @action(methods=["get"], detail=False)
    def running(self, request):
        response = {
            game.pk: GameSerializer(game).data for game in Game.objects.filter(status=Game.RUNNING, is_archived=False)
        }
        return Response(response)

    @action(
        methods=["post"],
        detail=False,
        serializer_class=GameIdsSerializer,
        permission_classes=(CanDeleteGame,),
    )
    def delete_games(self, request):
        game_ids = request.data.getlist("game_ids")
        games = (
            Game.objects.filter(
                pk__in=game_ids,
                game_class__teacher__school=request.user.userprofile.teacher.school,
                is_archived=False,
            )
            if request.user.userprofile.teacher.is_admin
            else Game.objects.filter(pk__in=game_ids, game_class__teacher__new_user=request.user, is_archived=False)
        )
        for game in games:
            game.is_archived = True  # mark as deleted/archived
            game.status = Game.STOPPED
            game.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def connection_parameters(request, game_id):
    """
    An API view which returns the correct connection settings required
    to run the game in different environments. These values will change
    depending on where the project is started (ie. local, etc).
    :param request: Django request object.
    :param game_id: Integer with the ID of the game.
    :return: JsonResponse object with the contents.
    """
    env_connection_settings = game_renderer.get_environment_connection_settings(game_id)

    avatar_id, response = get_avatar_id(request.user, game_id)

    if avatar_id:
        env_connection_settings.update({"avatar_id": avatar_id})
        return JsonResponse(env_connection_settings)
    else:
        return response


class GameTokenView(APIView):
    """
    View to Game tokens, used to prove a request comes from a game.
    """

    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = (GameHasToken,)

    def get(self, request, id):
        """
        After the initial token request, we need to check where the
        request comes from. So for subsequent requests we verify that
        they came from the token-holder.
        """
        game = get_object_or_404(Game, id=id)
        self.check_object_permissions(self.request, game)
        return Response(data={"token": game.auth_token})

    def patch(self, request, id):
        game = get_object_or_404(Game, id=id)
        self.check_object_permissions(self.request, game)
        try:
            game.auth_token = request.data["token"]
            game.save()
            return Response(status=status.HTTP_200_OK)
        except KeyError:
            return Response(status=status.HTTP_403_FORBIDDEN)


@ensure_csrf_cookie
def watch_game(request, id):
    game = get_object_or_404(Game, id=id)
    if not game.can_user_play(request.user):
        raise Http404

    game.status = Game.RUNNING
    game.save()
    return game_renderer.render_game(request, game)


def get_avatar_id(user: User, game_id) -> Tuple[int, HttpResponse]:
    avatar_id = None
    response = Response(status=status.HTTP_200_OK)

    try:
        avatar_id = game_renderer.get_avatar_id_from_user(user=user, game_id=game_id)
    except UserCannotPlayGameException:
        LOGGER.warning("HTTP 401 returned. User {} unauthorised to play.".format(user.id))
        response = HttpResponse("User unauthorized to play", status=401)
    except Avatar.DoesNotExist:
        LOGGER.warning("Avatar does not exist for user {} in game {}".format(user.id, game_id))
        response = HttpResponse("Avatar does not exist for this user", status=404)
    except Http404 as e:
        response = HttpResponse("Game does not exist", status=404)
    except Exception as e:
        LOGGER.error(f"Unknown error occurred while getting connection parameters: {e}")
        response = HttpResponse("Unknown error occurred when getting the current avatar", status=500)

    return avatar_id, response
