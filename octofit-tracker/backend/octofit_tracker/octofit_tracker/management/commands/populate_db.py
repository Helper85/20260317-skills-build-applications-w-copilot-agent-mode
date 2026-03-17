from datetime import timedelta

from django.core.management.base import BaseCommand
from django.utils import timezone

from octofit_tracker.models import Activity, LeaderboardEntry, Team, User, Workout


class Command(BaseCommand):
    help = 'octofit_db 데이터베이스에 테스트 데이터를 입력합니다.'

    def handle(self, *args, **options):
        now = timezone.now()

        Workout.objects.all().delete()
        LeaderboardEntry.objects.all().delete()
        Activity.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        Team.objects.create(
            name='marvel 팀',
            city='New York',
            motto='Avengers, assemble your fitness streak.',
            total_points=1900,
        )
        Team.objects.create(
            name='dc 팀',
            city='Gotham',
            motto='Train in the shadows, lead on the board.',
            total_points=1800,
        )

        users = [
            User.objects.create(
                full_name='Peter Parker',
                hero_alias='Spider-Man',
                email='spiderman@octofit.test',
                team_name='marvel 팀',
                favorite_workout='Web Sprint Intervals',
                points=980,
                joined_at=now - timedelta(days=30),
            ),
            User.objects.create(
                full_name='Carol Danvers',
                hero_alias='Captain Marvel',
                email='captainmarvel@octofit.test',
                team_name='marvel 팀',
                favorite_workout='Photon Power Circuit',
                points=920,
                joined_at=now - timedelta(days=24),
            ),
            User.objects.create(
                full_name='Bruce Wayne',
                hero_alias='Batman',
                email='batman@octofit.test',
                team_name='dc 팀',
                favorite_workout='Batcave Strength Block',
                points=910,
                joined_at=now - timedelta(days=28),
            ),
            User.objects.create(
                full_name='Diana Prince',
                hero_alias='Wonder Woman',
                email='wonderwoman@octofit.test',
                team_name='dc 팀',
                favorite_workout='Amazon Endurance Run',
                points=890,
                joined_at=now - timedelta(days=26),
            ),
        ]

        Activity.objects.bulk_create(
            [
                Activity(
                    user_email='spiderman@octofit.test',
                    hero_alias='Spider-Man',
                    activity_type='Rooftop HIIT',
                    duration_minutes=42,
                    calories_burned=510,
                    performed_at=now - timedelta(days=1),
                ),
                Activity(
                    user_email='captainmarvel@octofit.test',
                    hero_alias='Captain Marvel',
                    activity_type='Cosmic Row Session',
                    duration_minutes=38,
                    calories_burned=470,
                    performed_at=now - timedelta(days=2),
                ),
                Activity(
                    user_email='batman@octofit.test',
                    hero_alias='Batman',
                    activity_type='Night Ops Strength',
                    duration_minutes=55,
                    calories_burned=600,
                    performed_at=now - timedelta(days=1, hours=4),
                ),
                Activity(
                    user_email='wonderwoman@octofit.test',
                    hero_alias='Wonder Woman',
                    activity_type='Lasso Mobility Flow',
                    duration_minutes=48,
                    calories_burned=530,
                    performed_at=now - timedelta(days=3),
                ),
            ]
        )

        LeaderboardEntry.objects.bulk_create(
            [
                LeaderboardEntry(
                    hero_alias='Spider-Man',
                    email='spiderman@octofit.test',
                    team_name='marvel 팀',
                    score=980,
                    rank=1,
                    streak_days=12,
                ),
                LeaderboardEntry(
                    hero_alias='Captain Marvel',
                    email='captainmarvel@octofit.test',
                    team_name='marvel 팀',
                    score=920,
                    rank=2,
                    streak_days=9,
                ),
                LeaderboardEntry(
                    hero_alias='Batman',
                    email='batman@octofit.test',
                    team_name='dc 팀',
                    score=910,
                    rank=3,
                    streak_days=10,
                ),
                LeaderboardEntry(
                    hero_alias='Wonder Woman',
                    email='wonderwoman@octofit.test',
                    team_name='dc 팀',
                    score=890,
                    rank=4,
                    streak_days=8,
                ),
            ]
        )

        Workout.objects.bulk_create(
            [
                Workout(
                    title='Web Sprint Intervals',
                    hero_alias='Spider-Man',
                    recommended_team='marvel 팀',
                    category='Cardio',
                    intensity='High',
                    duration_minutes=35,
                    description='Short explosive runs and agility ladder repeats.',
                ),
                Workout(
                    title='Photon Power Circuit',
                    hero_alias='Captain Marvel',
                    recommended_team='marvel 팀',
                    category='Strength',
                    intensity='High',
                    duration_minutes=40,
                    description='Full-body power blocks with battle rope finisher.',
                ),
                Workout(
                    title='Batcave Strength Block',
                    hero_alias='Batman',
                    recommended_team='dc 팀',
                    category='Strength',
                    intensity='Medium',
                    duration_minutes=45,
                    description='Compound lifts followed by core stability work.',
                ),
                Workout(
                    title='Amazon Endurance Run',
                    hero_alias='Wonder Woman',
                    recommended_team='dc 팀',
                    category='Endurance',
                    intensity='Medium',
                    duration_minutes=50,
                    description='Tempo run with mobility cooldown for recovery.',
                ),
            ]
        )

        self.stdout.write(self.style.SUCCESS('octofit_db 테스트 데이터 적재 완료'))
