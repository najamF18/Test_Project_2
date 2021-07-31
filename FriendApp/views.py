from django.shortcuts import render
from .models import FriendList, FriendRequest
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, RetrieveAPIView, ListCreateAPIView
from .serializers import FriendListSerializer, RequestSerializer, FriendRequestSerializer
from rest_framework.response import Response
from LoginApp.models import User
# Create your views here.

class ListAllFriendsView(ListAPIView):
    queryset = FriendList.objects.all()
    serializer_class = FriendListSerializer
    
    def get(self, request):
        obj = FriendList.objects.filter(user=request.user)
        friend_list_serializer = self.serializer_class(obj, many=True, context={"request":request})
        if friend_list_serializer:
            # when we user 'filter' while querying data we need to return friend_list_serializer.data so data is in json
            return Response(friend_list_serializer.data)
        else:
            return Response({"message":"something went wrong"})
        
class SendFriendRequestView(CreateAPIView):
    queryset = FriendRequest.objects.all()
    serializer_class = RequestSerializer
    
    def post(self, request):
        try:
            receiver = User.objects.get(id=request.data["id"])
            send_request = FriendRequest.objects.get_or_create(sender=request.user, receiver=receiver)
            return Response({"message":"Friend Request Sent"})
        except Exception as e:
            return Response(e)

class ListAllFriendRequestView(ListAPIView):
    queryset = FriendRequest.objects.all()
    serializer_class = FriendRequestSerializer
    
    def get(self,request):
        obj = FriendRequest.objects.filter(receiver=request.user)  
        print(request.user)
        friend_request_list_serializer = self.serializer_class(obj, many=True, context={"request":request})
        if friend_request_list_serializer:
            # when we user 'filter' while querying data we need to return friend_list_serializer.data so data is in json
            return Response(friend_request_list_serializer.data)
        else:
            return Response({"message":"something went wrong"})
        
class AcceptRequestView(APIView):
    serializer_class = RequestSerializer
    
    def post(self, request):
        try:
            friend_request = FriendRequest.objects.get(id=request.data["id"])
            my_friend_list = FriendList.objects.get_or_create(user=request.user)
            print(my_friend_list[0].user)
            my_friend_list[0].friends.add(friend_request.sender)
            sender_friend_list = FriendList.objects.get_or_create(user=friend_request.sender)
            sender_friend_list[0].friends.add(request.user)
            friend_request.delete()
            return Response({"message": "Friend Request Accepted"})
        except Exception as e:
            return Response({":message":"Something went wrong"})
        
class DeleteRequestView(APIView):
    serializer_class = RequestSerializer
    
    def post(self, request):
        try:
            friend_request = FriendRequest.objects.get(id=request.data["id"])
            friend_request.delete()
            return Response({"message": "Friend Request Deleted"})
        except Exception as e:
            return Response({":message":"Something went wrong"})
    
class UnfriendView(APIView):
    serializer_class = RequestSerializer
    
    def get(self, request, user_id):
        try:
            my_friend_list = FriendList.objects.get_or_create(user=request.user)
            user_to_remove = User.objects.get(id=user_id)
            my_friend_list[0].friends.remove(user_to_remove)
            removee_friend_list = FriendList.objects.get_or_create(user=user_to_remove)
            removee_friend_list[0].friends.remove(request.user)
            return Response({"message": "Unfriended Successfully"})
        except Exception as e:
            return Response({":message":"Something went wrong"})


        
        
