from django.db import models

# Create your models here.
class StaffLogin(models.Model):
    Email = models.EmailField()
    Password = models.CharField(max_length=10)

    def __str__(self):
        return self.Email
