from django.db import models
from django.contrib.auth.hashers import make_password
import uuid
from django.contrib.auth.models import AbstractUser, BaseUserManager

# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field is required")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        return self.create_user(email, password, **extra_fields)


# Creating a custom user model
class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # username = models.CharField(max_length=260, unique=True) 
    email = models.EmailField(unique=True, max_length=260)
    password = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    username = None
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email
    
    
    # REQUIRED_FIELDS = ['email']
    def save(self, *args, **kwargs):
        # Ensure password is made hashed before saving to project password from been used
        if not self.password.startswith('pbkdf2_sha256$'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email

# Creating task category model  
class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=260, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='categories') # Enable users to have their own categories
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
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks") # Ensuring each task belongs to a user
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name="tasks") # Referencing the Category 
    title = models.CharField(max_length=260)
    description = models.TextField()
    due_date = models.DateField()
    status = models.CharField(max_length=60, choices=STATUS_CHOICES, default='pending')
    priority = models.CharField(max_length=60, choices=PRIORITY_CHOICES, default='medium')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.status}"
   
    
# Creating task reminder model 
class TaskReminder(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    task = models.ForeignKey(Task, on_delete=models.CASCADE) # Referencing the Task model 
    reminder_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reminder for {self.task.title} at {self.reminder_at}"