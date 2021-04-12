from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

class Customer(models.Model):
    fullname = models.TextField(max_length=80)
    email = models.EmailField()
    phone = models.TextField(max_length=11)
    password = models.TextField(max_length=10)
    age = models.IntegerField()

    def __str__(self):
        return self.user.username

class Staff(models.Model):
    fullname = models.TextField(max_length=80)
    email = models.EmailField()
    phone = models.TextField(max_length=11)
    password = models.TextField(max_length=10)
    age = models.IntegerField()

    def __str__(self):
        return self.user.username
