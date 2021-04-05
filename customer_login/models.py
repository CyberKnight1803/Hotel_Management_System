from django.db import models

# Create your models here.
class Customer(models.Model):
    fullname = models.TextField(max_length=80)
    email = models.EmailField()
    phone = models.TextField(max_length=11)
    password = models.TextField(max_length=10)
    age = models.IntegerField()
    