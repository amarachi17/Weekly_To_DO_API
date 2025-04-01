from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import RegisterView, LoginView, CategoryListView, CategoryDetailView, TaskListView, TaskDetailView, TaskReminderListView, TaskReminderDetailView

# Creating urlpatterns 
urlpatterns = [
    # Authentiations
    path('register/', RegisterView.as_view(), name='register-user'),
    path('login/', LoginView.as_view(), name='login-user'),
    path('token-refresh/', TokenRefreshView.as_view(), name='token-refresh'),

    # Category API
    path('categories/', CategoryListView.as_view(), name='category-list-create'),
    path('categories/<uuid:pk>/', CategoryDetailView.as_view(), name='category-detail'),

    # Task API
    path('tasks/', TaskListView.as_view(), name='task-list-create'),
    path('tasks/<uuid:pk>/', TaskDetailView.as_view(), name='task-detail'),

    # Task Reminder API
    path('reminders/', TaskReminderListView.as_view(), name='reminder-list-create'),
    path('reminders/<uuid:pk>/', TaskReminderDetailView, name='reminder-detail'),
]
