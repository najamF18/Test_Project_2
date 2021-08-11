from rest_framework import serializers
from drf_spectacular.utils import extend_schema_serializer, OpenApiParameter, OpenApiExample
from .models import(
    Message,
    ChatThread,
    photos
)
from LoginApp.serializers import UserSerializer
from django.db import models

class PhotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = photos
        fields = ('images',)


class ChatThreadSerializer(serializers.ModelSerializer):
    
    sender = serializers.StringRelatedField()
    receiver = serializers.StringRelatedField()
    
    class Meta:
        model = ChatThread
        fields = '__all__'
        

class MessageSerializer(serializers.ModelSerializer):
    # profile_photo = serializers.ListField(child=serializers.ImageField( max_length=100000, allow_empty_file=True, use_url=True), required=False)
    attachments = PhotosSerializer(many=True, required=False)
    
    class Meta:
        model = Message
        # fields = "__all__"
        exclude = ('sender',)
        
    def create(self, validated_data):
        pictures_data = validated_data.pop('attachments')
        print("this is profile photos popped", pictures_data)
        validated_data["sender"] = self.context["request"].user
        msg = Message.objects.create(**validated_data)
        # print(msg.message_pics.profile_photos)
        for image_data in pictures_data:
            photos.objects.create(message=msg, images=image_data)
        return msg