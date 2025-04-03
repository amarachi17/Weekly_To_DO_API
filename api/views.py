from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import make_password, check_password
from .models import User, Category, Task, TaskReminder
from .serializers import RegisterUserSerializers, LoginUserSerializers, TaskUserSerializers, TaskReminderSerializers, CategoryUserSerializers, CustomTokenObtainPairSerializer
from django.contrib.auth import get_user_model 
from rest_framework_simplejwt.views import TokenObtainPairView


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
        
        user = serializer.validated_data["user"]
        refresh = RefreshToken.for_user(user)
        return Response({
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "user": {
                "id": user.id,
                "email": user.email,
            },
        }, status =status.HTTP_200_OK)
        # return Response(serializer.validated_data, status=status.HTTP_200_OK)

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
        # user = self.request.user
        # if not isinstance(user, get_user_model()):
        #     user = get_user_model().objects.get(id=user.id)
        # serializer.save(user=user)

        # serializer.save(user=self.request.user)

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
    
    def perform_create(self, serializer):
        task = serializer.validated_data.get("task")
        if task.user != self.request.user:
            return Response({"error": "You can only set reminders for your tasks."}, status=status.HTTP_403_FOEBIDDEN)
        serializer.save() 

# Creating view to retrieve, update, delete a task reminder 
class TaskReminderDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskReminderSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return TaskReminder.objects.filter(task__user=self.request.user)

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
