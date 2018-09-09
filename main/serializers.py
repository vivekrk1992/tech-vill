from rest_framework import serializers
from main.models import User, UserProfile, UserType


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class UserTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserType
        fields = ('id', 'name')


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_type = UserTypeSerializer(read_only=True)

    class Meta:
        model = UserProfile
        fields = ('id', 'user', 'user_type')