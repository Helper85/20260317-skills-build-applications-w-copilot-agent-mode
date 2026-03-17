from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Activity, LeaderboardEntry, Team, User, Workout
from .serializers import (
    ActivitySerializer,
    LeaderboardEntrySerializer,
    TeamSerializer,
    UserSerializer,
    WorkoutSerializer,
)

COLLECTION_ENDPOINTS = {
    'users': '/api/users/',
    'teams': '/api/teams/',
    'activities': '/api/activities/',
    'leaderboard': '/api/leaderboard/',
    'workouts': '/api/workouts/',
}


def get_api_base_url(request):
    codespace_name = request.META.get('CODESPACE_NAME')
    if codespace_name:
        return f'https://{codespace_name}-8000.app.github.dev'
    return 'http://localhost:8000'


@api_view(['GET'])
def api_root(request, base_url=None):
    resolved_base_url = base_url or get_api_base_url(request)
    return Response(
        {name: f'{resolved_base_url}{path}' for name, path in COLLECTION_ENDPOINTS.items()},
        status=status.HTTP_200_OK,
    )


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer


class LeaderboardEntryViewSet(viewsets.ModelViewSet):
    queryset = LeaderboardEntry.objects.all()
    serializer_class = LeaderboardEntrySerializer


class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
