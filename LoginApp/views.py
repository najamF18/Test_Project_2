from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from rest_framework.views import APIView
from django.views.generic import ListView, DetailView, View
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, RetrieveAPIView, ListCreateAPIView
from .models import User
from rest_framework.reverse import reverse
from .serializers import ( 
                          UserSerializer, 
                          LoginSerializer,
                          ChangePasswordSerializer,
                          RequestChangePasswordSerializer
                        )
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate,login,logout
from django.core.mail import EmailMessage

# Create your views here.
    
class RegisterUserView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    
    def post(self, request):
        response = dict()
        user_serializer = self.serializer_class(data=request.data, context={'request': request})
        if user_serializer.is_valid():
            user = user_serializer.save()
            response["email"] = user.email
            response["message"] = "User registered successfully"
            return Response(response)
            
    
class LoginView(APIView):

    serializer_class = LoginSerializer
    
    def post(self, request):
        data = request.data
        try:
            user = User.objects.get(email=data["email"])
        except Exception as e:
            print(e)
        user_auth = authenticate(email=data["email"], password=data["password"])
        print(request.user)
        if user_auth:
            login(request, user)
            print(request.user)
            response = dict()
            response["message"] = "User logged in succesfully"
            return Response(response)
        else:
            
            return Response({"message":"Credentials provided, are not correct"})
        
class LogoutView(APIView):
    
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
            return Response({"message": "successfully logged out"})
        else:
            return Response({"message":"No user is logged in"})
        
        
class RequestChangePasswordView(APIView):
    
    serializer_class = RequestChangePasswordSerializer 
    def post(self, request):
        try:
            user = User.objects.get(email=request.data["email"])
            if user:
                print("user")
                url_password_change = reverse("change_password", request=request, args=["ad@ad.com"])
                email = EmailMessage('Password change request', url_password_change, to=[user.email])
                email.send()
                return Response({"message" : "check your mail we have sent you a link to change password"})
        except Exception as e:
            print(e)
            return Response({"message":"not a valid user"})

class ChangePasswordView(APIView):
    
    serializer_class = ChangePasswordSerializer
    
    def post(self, request, email):
        user = User.objects.get(email=email)
        if user:
            print(user.email)
            print("new password ", request.data["new_password"])
            print("confirm new password ", request.data["confirm_new_password"])
            if request.data["new_password"] == request.data["confirm_new_password"]:
                # user.password = request.data["new_password"]
                # user_new_pass = user.save()
                user.set_password(user.password)
                user.save()
                
            return Response({"message": "Password Changed successfully"})
        
class ListLoggedInUser(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def get(self, request):
        try:
            logged_user = User.objects.get(email=request.user.email)
            if logged_user:
                response = self.serializer_class(logged_user, context={"request": request}).data
            return Response(response)
        except Exception as e:
            return Response(e)

        
        
        
    
        
    
    
    