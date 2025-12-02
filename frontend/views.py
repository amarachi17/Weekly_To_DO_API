from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'frontend/base.html')

def login_page(request): 
    return render(request, 'frontend/login.html')

def register_page(request): 
    return render(request, 'frontend/register.html')

def dashboard_page(request): 
    return render(request, 'frontend/dashboard.html')

def categories_page(request): 
    return render(request, 'frontend/categories.html')

def tasks_page(request): 
    return render(request, 'frontend/tasks.html')

def reminders_page(request): 
    return render(request, 'frontend/reminders.html')