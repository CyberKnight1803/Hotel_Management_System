from django.db import models
from django.utils import timezone

# Create your models here.
class Reservation(models.Model):
    reservationID = models.AutoField(primary_key=True)
    checkin = models.DateField()
    checkout = models.DateField()
    adults = models.PositiveIntegerField()
    children = models.PositiveIntegerField()
    roomtype = models.TextField(max_length=25)
    rooms = models.PositiveIntegerField()
    email = models.EmailField(null=True)
    date_requested = models.DateTimeField(default=timezone.now)
