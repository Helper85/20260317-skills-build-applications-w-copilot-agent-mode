import os

from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ActivityViewSet, LeaderboardEntryViewSet, TeamViewSet, UserViewSet, WorkoutViewSet, api_root

app_name = 'octofit_tracker'

codespace_name = os.environ.get('CODESPACE_NAME')
if codespace_name:
    api_base_url = f"https://{codespace_name}-8000.app.github.dev"
else:
    api_base_url = 'http://localhost:8000'

router = DefaultRouter()
router.register('users', UserViewSet, basename='user')
router.register('teams', TeamViewSet, basename='team')
router.register('activities', ActivityViewSet, basename='activity')
router.register('leaderboard', LeaderboardEntryViewSet, basename='leaderboard')
router.register('workouts', WorkoutViewSet, basename='workout')

urlpatterns = [
    path('', api_root, {'base_url': api_base_url}, name='root'),
    path('admin/', admin.site.urls),
    path('api/', api_root, {'base_url': api_base_url}, name='api-root'),
    path('api/', include(router.urls)),
]

