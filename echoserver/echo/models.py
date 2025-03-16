from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator


class Books(models.Model):
    name = models.CharField(max_length=80, blank=True, null=True)
    author = models.CharField(max_length=80, blank=True, null=True)
    cost = models.FloatField(blank=True, null=True)
    genre = models.CharField(max_length=80, blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'books'


class Users(AbstractUser):
    ROLES = (
        ('user', 'Обычный пользователь'),
        ('admin', 'Администратор'),
    )
    
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=ROLES, default='user')

    def __str__(self):
        return self.login
    
    class Meta:
        db_table = 'users'