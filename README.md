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
    )
}

# api - Models.py file
## Created all models for the database
Class User - User model to store user information and hash user password
Class Category - Category to store category information
Class Task - Add task status and priority
Class Task Reminder - Set reminder for each task