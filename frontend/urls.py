from django.urls import path
from django.shortcuts import render

urlpatterns = [
    path("login/", lambda request: render(request, "frontend/login.html"), name="login-page"),
    path("register/", lambda request: render(request, "frontend/register.html"), name="register-page"),
    path("dashboard/", lambda request: render(request, "frontend/dashboard.html"), name="dashboard"),

    path("categories/", lambda request: render(request, "frontend/categories.html"), name="categories"),
    path("tasks/", lambda request: render(request, "frontend/tasks.html"), name="tasks"),
    path("reminders/", lambda request: render(request, "frontend/reminders.html"), name="reminders"),

]
