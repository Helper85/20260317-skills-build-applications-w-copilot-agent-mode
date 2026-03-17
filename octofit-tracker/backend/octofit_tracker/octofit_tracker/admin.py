from django.contrib import admin

from .models import Activity, LeaderboardEntry, Team, User, Workout


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
	list_display = ('name', 'city', 'total_points')
	search_fields = ('name', 'city', 'motto')


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
	list_display = ('hero_alias', 'full_name', 'email', 'team_name', 'points')
	search_fields = ('hero_alias', 'full_name', 'email', 'team_name')


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
	list_display = ('hero_alias', 'activity_type', 'duration_minutes', 'calories_burned', 'performed_at')
	search_fields = ('hero_alias', 'user_email', 'activity_type')


@admin.register(LeaderboardEntry)
class LeaderboardEntryAdmin(admin.ModelAdmin):
	list_display = ('rank', 'hero_alias', 'team_name', 'score', 'streak_days')
	search_fields = ('hero_alias', 'email', 'team_name')


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
	list_display = ('title', 'hero_alias', 'recommended_team', 'category', 'intensity', 'duration_minutes')
	search_fields = ('title', 'hero_alias', 'recommended_team', 'category')

