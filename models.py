from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Professional Roles for RBAC
    class Roles(models.TextChoices):
        ADMIN = 'ADMIN', 'Admin'
        MODERATOR = 'MODERATOR', 'Moderator'
        USER = 'USER', 'User'
        PREMIUM = 'PREMIUM', 'Premium User'

    email = models.EmailField(unique=True)
    role = models.CharField(
        max_length=20, 
        choices=Roles.choices, 
        default=Roles.USER
    )
    bio = models.TextField(blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    # Use email for login instead of username
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
