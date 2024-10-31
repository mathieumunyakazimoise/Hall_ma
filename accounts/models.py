from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .manager import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True, null=False)
    username = models.CharField(max_length=255, null=False)
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    student_id = models.CharField(max_length=100, unique=True, null=True)
   
    phone = models.CharField(max_length=50, null=True, blank=True)
   
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
   
    date = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
   
    USERNAME_FIELD = 'email'
   
    REQUIRED_FIELDS = [
        'username',
        'first_name',
        'last_name'
    ]
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('admin', 'Administrator'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='student')
   
    # Custom user manager object
    objects = UserManager()


    def __str__(self):
        return self.email


    # Property to get user's full name
    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
