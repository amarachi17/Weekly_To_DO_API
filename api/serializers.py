from rest_framework import serializers
from django.contrib.auth.hashers import make_password
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