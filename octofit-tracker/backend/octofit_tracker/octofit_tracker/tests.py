from bson import ObjectId
from django.contrib import admin
from django.test import RequestFactory, SimpleTestCase
from django.urls import reverse

from .admin import ActivityAdmin, LeaderboardEntryAdmin, TeamAdmin, UserAdmin, WorkoutAdmin
from .models import Activity, LeaderboardEntry, Team, User, Workout
from .serializers import (
    ActivitySerializer,
    LeaderboardEntrySerializer,
    TeamSerializer,
    UserSerializer,
    WorkoutSerializer,
)
from .views import (
    ActivityViewSet,
    LeaderboardEntryViewSet,
    TeamViewSet,
    UserViewSet,
    WorkoutViewSet,
    api_root,
)


class SerializerCoverageTests(SimpleTestCase):
    def test_team_serializer_outputs_string_object_id(self):
        team = Team(
            id=ObjectId(),
            name='marvel 팀',
            city='New York',
            motto='Assemble.',
            total_points=1900,
        )

        data = TeamSerializer(team).data

        self.assertEqual(data['name'], 'marvel 팀')
        self.assertIsInstance(data['id'], str)

    def test_user_serializer_covers_user_collection(self):
        user = User(
            id=ObjectId(),
            full_name='Peter Parker',
            hero_alias='Spider-Man',
            email='spiderman@octofit.test',
            team_name='marvel 팀',
            favorite_workout='Web Sprint Intervals',
            points=980,
            joined_at='2026-02-15T01:59:31Z',
        )

        data = UserSerializer(user).data

        self.assertEqual(data['email'], 'spiderman@octofit.test')
        self.assertIsInstance(data['id'], str)

    def test_activity_serializer_covers_activity_collection(self):
        activity = Activity(
            id=ObjectId(),
            user_email='spiderman@octofit.test',
            hero_alias='Spider-Man',
            activity_type='Rooftop HIIT',
            duration_minutes=42,
            calories_burned=510,
            performed_at='2026-03-16T01:59:31Z',
        )

        data = ActivitySerializer(activity).data

        self.assertEqual(data['activity_type'], 'Rooftop HIIT')
        self.assertIsInstance(data['id'], str)

    def test_leaderboard_serializer_covers_leaderboard_collection(self):
        entry = LeaderboardEntry(
            id=ObjectId(),
            hero_alias='Spider-Man',
            email='spiderman@octofit.test',
            team_name='marvel 팀',
            score=980,
            rank=1,
            streak_days=12,
        )

        data = LeaderboardEntrySerializer(entry).data

        self.assertEqual(data['rank'], 1)
        self.assertIsInstance(data['id'], str)

    def test_workout_serializer_covers_workout_collection(self):
        workout = Workout(
            id=ObjectId(),
            title='Web Sprint Intervals',
            hero_alias='Spider-Man',
            recommended_team='marvel 팀',
            category='Cardio',
            intensity='High',
            duration_minutes=35,
            description='Short explosive runs and agility ladder repeats.',
        )

        data = WorkoutSerializer(workout).data

        self.assertEqual(data['title'], 'Web Sprint Intervals')
        self.assertIsInstance(data['id'], str)


class ApiAndRoutingTests(SimpleTestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_api_root_lists_all_supported_collections(self):
        request = self.factory.get('/api/')

        response = api_root(request, base_url='http://localhost:8000')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.data,
            {
                'users': 'http://localhost:8000/api/users/',
                'teams': 'http://localhost:8000/api/teams/',
                'activities': 'http://localhost:8000/api/activities/',
                'leaderboard': 'http://localhost:8000/api/leaderboard/',
                'workouts': 'http://localhost:8000/api/workouts/',
            },
        )

    def test_router_registers_all_collection_routes(self):
        self.assertEqual(reverse('user-list'), '/api/users/')
        self.assertEqual(reverse('team-list'), '/api/teams/')
        self.assertEqual(reverse('activity-list'), '/api/activities/')
        self.assertEqual(reverse('leaderboard-list'), '/api/leaderboard/')
        self.assertEqual(reverse('workout-list'), '/api/workouts/')

    def test_viewsets_use_expected_models(self):
        self.assertIs(TeamViewSet.queryset.model, Team)
        self.assertIs(UserViewSet.queryset.model, User)
        self.assertIs(ActivityViewSet.queryset.model, Activity)
        self.assertIs(LeaderboardEntryViewSet.queryset.model, LeaderboardEntry)
        self.assertIs(WorkoutViewSet.queryset.model, Workout)


class AdminRegistrationTests(SimpleTestCase):
    def test_admin_site_registers_all_supported_models(self):
        self.assertIsInstance(admin.site._registry[Team], TeamAdmin)
        self.assertIsInstance(admin.site._registry[User], UserAdmin)
        self.assertIsInstance(admin.site._registry[Activity], ActivityAdmin)
        self.assertIsInstance(admin.site._registry[LeaderboardEntry], LeaderboardEntryAdmin)
        self.assertIsInstance(admin.site._registry[Workout], WorkoutAdmin)