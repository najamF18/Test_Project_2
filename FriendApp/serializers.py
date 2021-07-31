from rest_framework import serializers
from drf_spectacular.utils import extend_schema_serializer, OpenApiParameter, OpenApiExample
from .models import(
    FriendList,
    FriendRequest
)
from LoginApp.serializers import UserSerializer
from django.db import models


class FriendListSerializer(serializers.ModelSerializer):
    
    friends = UserSerializer(many=True)
    
    class Meta:
        model = FriendList
        fields ='__all__'
        # depth = 1
        
    def to_representation(self, instance):
        rep = super(FriendListSerializer, self).to_representation(instance)
        rep['user'] = instance.user.email
        return rep
        
class FriendRequestSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = FriendRequest
        fields ='__all__'
        
class RequestSerializer(serializers.Serializer):
    id = serializers.IntegerField()
        