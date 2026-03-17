from rest_framework import serializers

from .models import Activity, LeaderboardEntry, Team, User, Workout


class ObjectIdStringMixin(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    def get_id(self, obj):
        return str(obj.pk)


class TeamSerializer(ObjectIdStringMixin):
    class Meta:
        model = Team
        fields = '__all__'
        read_only_fields = ('id',)


class UserSerializer(ObjectIdStringMixin):
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ('id',)


class ActivitySerializer(ObjectIdStringMixin):
    class Meta:
        model = Activity
        fields = '__all__'
        read_only_fields = ('id',)


class LeaderboardEntrySerializer(ObjectIdStringMixin):
    class Meta:
        model = LeaderboardEntry
        fields = '__all__'
        read_only_fields = ('id',)


class WorkoutSerializer(ObjectIdStringMixin):
    class Meta:
        model = Workout
        fields = '__all__'
        read_only_fields = ('id',)
