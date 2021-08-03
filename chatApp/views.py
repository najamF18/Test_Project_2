from django.shortcuts import render
from .models import Message, ChatThread
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, RetrieveAPIView, ListCreateAPIView
from .serializers import MessageSerializer, ChatThreadSerializer, SendMessageSerializer
from rest_framework.response import Response
from LoginApp.models import User
from django.db.models import Q
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class ListAllThreadOfLoggedUser(ListAPIView):
    queryset = ChatThread.objects.all()
    serializer_class = ChatThreadSerializer
    authentications_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        # if you want to execute 'OR' in django query that is how
        thread = ChatThread.objects.filter(Q(sender=request.user) | Q(receiver=request.user))
        thread_serialized = self.serializer_class(thread, many=True, context={"request":request})
        return Response(thread_serialized.data)
    
class ListAllMessagesInThread(ListAPIView):
    queryset = ChatThread.objects.all()
    serializer_class = MessageSerializer
    authentications_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, chat_id):
        messages = ChatThread.objects.get(id=chat_id)
        messages_serialized = self.serializer_class(messages.thread, many=True, context={"request":request})
        return Response(messages_serialized.data)
        
class SendMessageInChatThread(APIView):
    
    serializer_class = SendMessageSerializer
    authentications_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request, chat_id):
        thread = ChatThread.objects.get(id=chat_id)
        msg = Message.objects.get_or_create(message=request.data["content"])
        thread.thread.add(msg[0])
        return Response({"status": "Your message has been sent"})