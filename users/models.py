from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(max_length=100, unique=True, verbose_name='почта')
    avatar = models.ImageField(upload_to='users/avatars', verbose_name='аватар', **NULLABLE)
    phone = models.CharField(max_length=20, verbose_name='телефон', **NULLABLE)
    country = models.CharField(max_length=20, verbose_name='страна', **NULLABLE)
    token = models.CharField(max_length=100, **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
