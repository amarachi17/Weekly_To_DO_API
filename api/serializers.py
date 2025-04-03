from rest_framework import serializers
from django.contrib.auth.hashers import make_password, check_password
from .models import User, Category, Task, TaskReminder
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# from django.contrib.auth import get_user_model 
# User = get_user_model()

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
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)


    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        # Validate data in a try except to catch bugs
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid email or password")
        
        if not check_password(password, user.password):
            raise serializers.ValidationError("Invalid email or password")
        
        data['user'] = user
        return data
        # Generate JWT TOKENS
        refresh = RefreshToken.for_user(user)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': {
                'id': user.id,
                'username': user.username,
                'email': user.email,
            }
        }

# Serializers for Category model 
class CategoryUserSerializers(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'user', 'created_at']

# Serializers for Task model 
class TaskUserSerializers(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    
    class Meta:
        model = Task
        fields = '__all__'

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user # User.objects.get(id=self.context['request'].user.id)
        return super().create(validated_data)

        # fields = ['id', 'category', 'title', 'description', 'due_date', 'status', 'priority', 'created_at', 'updated_at']
        # read_only_fields = ['user']
# Serializers for Task Reminder model.
class TaskReminderSerializers(serializers.ModelSerializer):
    class Meta:
        model = TaskReminder
        fields = ['id', 'task', 'reminder_at', 'created_at']

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            from django.contrib.auth import get_user_model
            User = get_user_model()
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                raise serializers.ValidationError("No active account found with given credentials")
            
            if not user.check_password(password):
                raise serializers.ValidationError("Incorrect Password")
            
            attrs["username"] = user.email
        return super().validate(attrs)