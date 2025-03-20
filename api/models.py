from django.db import models
from django.contrib.auth.hashers import make_password
import uuid

# Create your models here.

# Creating a custom user model
class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=260, unique=True)
    email = models.EmailField(unique=True, max_length=260)
    password = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # Ensure password is made hashed before saving to project password from been used
        if not self.password.startswith('pbkdf2_sha265$'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username

# Creating task category model  
class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=260, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE) # Enable users to have their own categories
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Creating task model 
class Task(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    PRIORITY_CHOICES = [
        ('high', 'High'),
        ('medium', 'Medium'),
        ('low', 'Low'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE) # Ensuring each task belongs to a user
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True) # Referencing the Category 
    title = models.CharField(max_length=260)
    description = models.TextField(blank=True)
    due_date = models.DateField()
    status = models.CharField(max_length=60, choices=STATUS_CHOICES, default='pending')
    priority = models.CharField(max_length=60, choices=PRIORITY_CHOICES, default='medium')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
# Creating task reminder model 
class TaskReminder(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    task = models.ForeignKey(Task, on_delete=models.CASCADE) # Referencing the Task model 
    reminder_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reminder for {self.task.title} at {self.reminder_at}"