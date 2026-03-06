from rest_framework import serializers
from .models import User, Team, Activity, Workout, Leaderboard
from bson import ObjectId


class ObjectIdField(serializers.Field):
    """
    Serializer field for MongoDB ObjectId values.

    - Converts ObjectId instances to strings for JSON responses.
    - Accepts string values on input and converts them back to ObjectId.
    """

    def to_representation(self, value):
        if value is None:
            return None
        return str(value)

    def to_internal_value(self, data):
        if data in (None, ""):
            return None
        try:
            return ObjectId(str(data))
        except Exception:
            raise serializers.ValidationError("Invalid ObjectId")


class UserSerializer(serializers.ModelSerializer):
    # Ensure MongoDB ObjectId primary key is serialized as a string
    id = ObjectIdField(read_only=True)

    class Meta:
        model = User
        fields = '__all__'


class TeamSerializer(serializers.ModelSerializer):
    # Ensure MongoDB ObjectId primary key is serialized as a string
    id = ObjectIdField(read_only=True)

    class Meta:
        model = Team
        fields = '__all__'


class ActivitySerializer(serializers.ModelSerializer):
    # Ensure MongoDB ObjectId primary key is serialized as a string
    id = ObjectIdField(read_only=True)

    class Meta:
        model = Activity
        fields = '__all__'


class WorkoutSerializer(serializers.ModelSerializer):
    # Ensure MongoDB ObjectId primary key is serialized as a string
    id = ObjectIdField(read_only=True)

    class Meta:
        model = Workout
        fields = '__all__'


class LeaderboardSerializer(serializers.ModelSerializer):
    # Ensure MongoDB ObjectId primary key is serialized as a string
    id = ObjectIdField(read_only=True)
    class Meta:
        model = Leaderboard
        fields = '__all__'
