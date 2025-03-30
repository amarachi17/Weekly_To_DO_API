# Weekly_To_DO_API
- cloned this repository

# Started a project
- django-admin startproject to_do_api.

# Started a app
- python manage.py startapp api

# Installed 
- Installed Django
- Installed Django RestFramework
- Installed Django RestFramework SimpleJWT

# Added Installed apps to Settings.py
- 'api',
- 'rest_framework',
- 'rest_framework_simplejwt',

# Added JWT Authentication to Settings.py file
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    )
}

# api - Models.py file
## Created all models for the database
Class User - User model to store user information and hash user password
Class Category - Category to store category information
Class Task - Add task status and priority
Class Task Reminder - Set reminder for each task

## Added access and refresh token life span to protect each users
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=2),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': True,
}

# Create Serializers.py
- Class RegisterUserSerializers - Registers User model in serializer and hash the password
- Class LoginUserSerializers - Login Users that has been registered and validates credentials before returning a JWT token.
- Class CategoryUserSerializers - Creating a serializer for category model
- Class TaskUserSerializers - Creating a serializer for Task model
- Class TaskReminderSerializer - Creating a serializer for Task Reminder model

## Creating Authentication views 
- Class RegisterView - Creating views for Register User Serializer
- Class LoginView - Creating views for Login User Serializer