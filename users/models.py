from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('donor', 'Donor'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='donor')

    def __str__(self):
        return self.username