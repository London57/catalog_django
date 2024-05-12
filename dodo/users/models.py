from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    username = models.CharField(
        max_length=20,
        unique=True,
    )
    password = models.CharField(
        max_length = 20,
        verbose_name='password'
    )
    class Meta:
        verbose_name = 'user'
        