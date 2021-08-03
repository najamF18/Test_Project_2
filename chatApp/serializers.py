from rest_framework import serializers
from drf_spectacular.utils import extend_schema_serializer, OpenApiParameter, OpenApiExample
from .models import(
    Message,
    ChatThread
)
from LoginApp.serializers import UserSerializer
from django.db import models

class MessageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Message
        fields = '__all__'

class ChatThreadSerializer(serializers.ModelSerializer):
    
    sender = serializers.StringRelatedField()
    receiver = serializers.StringRelatedField()
    message = MessageSerializer(many=True)
    
    class Meta:
        model = ChatThread
        fields = '__all__'
        
    
class SendMessageSerializer(serializers.Serializer):
    to_user = serializers.EmailField()
    content = serializers.CharField()