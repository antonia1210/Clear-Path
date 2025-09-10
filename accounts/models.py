from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ('USER', 'User'),
        ('CONTABIL', 'Contabil'),
        ('ADMIN', 'Admin'),
        ('ARHIEPISCOP', 'Arhiepiscop'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='USER')
    full_name = models.CharField(max_length=255)
    #assigned_church = models.ForeignKey(Church, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.username} ({self.role})"