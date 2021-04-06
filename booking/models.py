from django.db import models

# Create your models here.
class Bookings(models.Model):
    checkin = models.DateField()
    checkout = models.DateField()
    adults = models.IntegerField()
    children = models.IntegerField() 
    roomtype = models.TextField(max_length=15)
    rooms = models.IntegerField()
    email = models.EmailField(null=True)