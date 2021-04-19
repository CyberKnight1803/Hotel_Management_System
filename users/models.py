from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image

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

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    # def save(self):
    #     super().save()
    #     img = Image.open(self.image.path)
    #     if img.height > 300 or img.width >300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)
