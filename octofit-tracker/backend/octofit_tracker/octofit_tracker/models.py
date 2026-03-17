from bson import ObjectId
from djongo import models


class Team(models.Model):
    id = models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    name = models.CharField(max_length=100, unique=True)
    city = models.CharField(max_length=100)
    motto = models.CharField(max_length=255)
    total_points = models.IntegerField(default=0)

    class Meta:
        db_table = 'teams'
        ordering = ['name']
        verbose_name_plural = 'teams'

    def __str__(self):
        return self.name


class User(models.Model):
    id = models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    full_name = models.CharField(max_length=120)
    hero_alias = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    team_name = models.CharField(max_length=100)
    favorite_workout = models.CharField(max_length=120)
    points = models.IntegerField(default=0)
    joined_at = models.DateTimeField()

    class Meta:
        db_table = 'users'
        ordering = ['hero_alias']
        verbose_name_plural = 'users'

    def __str__(self):
        return self.hero_alias


class Activity(models.Model):
    id = models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    user_email = models.EmailField()
    hero_alias = models.CharField(max_length=120)
    activity_type = models.CharField(max_length=120)
    duration_minutes = models.IntegerField()
    calories_burned = models.IntegerField()
    performed_at = models.DateTimeField()

    class Meta:
        db_table = 'activities'
        ordering = ['-performed_at']
        verbose_name_plural = 'activities'

    def __str__(self):
        return f'{self.hero_alias} - {self.activity_type}'


class LeaderboardEntry(models.Model):
    id = models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    hero_alias = models.CharField(max_length=120)
    email = models.EmailField()
    team_name = models.CharField(max_length=100)
    score = models.IntegerField()
    rank = models.IntegerField()
    streak_days = models.IntegerField(default=0)

    class Meta:
        db_table = 'leaderboard'
        ordering = ['rank', '-score']
        verbose_name_plural = 'leaderboard entries'

    def __str__(self):
        return f'{self.rank}: {self.hero_alias}'


class Workout(models.Model):
    id = models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    title = models.CharField(max_length=120)
    hero_alias = models.CharField(max_length=120)
    recommended_team = models.CharField(max_length=100)
    category = models.CharField(max_length=120)
    intensity = models.CharField(max_length=50)
    duration_minutes = models.IntegerField()
    description = models.TextField()

    class Meta:
        db_table = 'workouts'
        ordering = ['title']
        verbose_name_plural = 'workouts'

    def __str__(self):
        return self.title
