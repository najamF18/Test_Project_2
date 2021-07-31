from django.shortcuts import render
from .models import Message, ChatThread
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, RetrieveAPIView, ListCreateAPIView
from .serializers import MessageSerializer, ChatThreadSerializer, SendMessageSerializer
from rest_framework.response import Response
from LoginApp.models import User
# Create your views here.

class ListAllThreadOfLoggedUser(ListAPIView):
    queryset = ChatThread.objects.all()
    serializer_class = ChatThreadSerializer
    
    def get(self, request):
        thread = ChatThread.objects.filter(sender=request.user)
        thread_serialized = self.serializer_class(thread, many=True, context={"request":request})
        return Response(thread_serialized.data)
    
class ListAllMessagesInThread(ListAPIView):
    queryset = ChatThread.objects.all()
    serializer_class = MessageSerializer
    
    def get(self, request, chat_id):
        messages = ChatThread.objects.get(id=chat_id)
        messages_serialized = self.serializer_class(messages.thread, many=True, context={"request":request})
        return Response(messages_serialized.data)
        
class SendMessageInChatThread(APIView):
    
    serializer_class = SendMessageSerializer
    
    def post(self, request, chat_id):
        thread = ChatThread.objects.get(id=chat_id)
        msg = Message.objects.get_or_create(message=request.data["content"])
        thread.thread.add(msg[0])
        return Response({"status": "Your message has been sent"})