from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("login/", views.login_page, name="login"),
    path("register/", views.register_page, name="register"),
    path("dashboard/", views.dashboard_page, name="dashboard"),

    path("categories/", views.categories_page, name="categories"),
    path("tasks/", views.tasks_page, name="tasks"),
    path("reminders/", views.reminders_page, name="reminders"),

]
