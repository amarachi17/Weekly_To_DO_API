from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import make_password, check_password
from .models import User, Category, Task, TaskReminder
from .serializers import RegisterUserSerializers, LoginUserSerializers, TaskUserSerializers, TaskReminderSerializers, CategoryUserSerializers

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

# Creating view to list and create categories    
class CategoryListView(generics.ListCreateAPIView):
    serializer_class = CategoryUserSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# Creating view to retrieve, update, delete a category
class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategoryUserSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)
    
# Creating view to list and create tasks
class TaskListView(generics.ListCreateAPIView):
    serializer_class = TaskUserSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# Creating view to retrieve, update, delete a task
class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskUserSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
    
# Creating view to list and create task reminders
class TaskReminderListView(generics.ListCreateAPIView):
    serializer_class = TaskReminderSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return TaskReminder.objects.filter(task__user=self.request.user)
    
# Creating view to retrieve, update, delete a task reminder 
class TaskReminderDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskReminderSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return TaskReminder.objects.filter(task__user=self.request.user)
    