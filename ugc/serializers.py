from rest_framework import serializers
from .models import UGCPost, Location
from user.models import CustomUser
from user.serializers import UserProfileSerializer


class UGCPostSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer(read_only=True)

    class Meta:
        model = UGCPost
        user = CustomUser
        fields = ['id', 'user', 'title', 'content', 'created_at', 'updated_at']


class LocationSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer(read_only=True)

    class Meta:
        model = Location
        user = CustomUser
        fields = ['id', 'user', 'name', 'coordinates']
