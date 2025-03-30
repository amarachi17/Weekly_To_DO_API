from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import make_password, check_password
from .models import User, Category, Task, TaskReminder
from .serializers import RegisterUserSerializers, LoginUserSerializers, TaskUserSerializers, TaskReminderSerializer, CategoryUserSerializers

# Create your views here.

# Creating views for Register User Serializer 
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterUserSerializers
    permission_classes = [AllowAny]

# Creating views for Login User Serializer 
class LoginView(generics.GenericAPIView):
    serializer_class = LoginUserSerializers
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
    
