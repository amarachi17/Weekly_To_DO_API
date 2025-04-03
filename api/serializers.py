from rest_framework import serializers
from django.contrib.auth.hashers import make_password, check_password
from .models import User, Category, Task, TaskReminder

# Serializer for new user registration, and hashes the password before saving.
class RegisterUserSerializers(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password']) # Make the password hashed
        return super().create(validated_data)
    
# Login Serializer for registered user, Validates credentials and returns JWT tokens.
class LoginUserSerializers(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)


    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        # Validate data in a try except to catch bugs
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid username or password")
        
        if not check_password(password, user.password):
            raise serializers.ValidationError("Invalid username or password")
        
        from rest_framework_simplejwt.tokens import RefreshToken
        refresh = RefreshToken.for_user(user)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

# Serializers for Category model 
class CategoryUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'user', 'created_at']

# Serializers for Task model 
class TaskUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'user', 'category', 'title', 'description', 'due_date', 'status', 'priority', 'created_at', 'updated_at']

# Serializers for Task Reminder model.
class TaskReminderSerializers(serializers.ModelSerializer):
    class Meta:
        model = TaskReminder
        fields = ['id', 'task', 'reminder_at', 'created_at']