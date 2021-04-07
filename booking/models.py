from django.db import models

# Create your models here.
class Booking(models.Model):
    checkin = models.DateField()
    checkout = models.DateField()
    adults = models.PositiveIntegerField()
    children = models.PositiveIntegerField()
    roomtype = models.TextField(max_length=15)
    rooms = models.PositiveIntegerField()
    email = models.EmailField(null=True)
