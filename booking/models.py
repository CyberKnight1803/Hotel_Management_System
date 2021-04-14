from django.db import models
from django.utils import timezone
from users.models import User

# Create your models here.
class Reservation(models.Model):
    ROOM_TYPE_CHOICES = (
      (1, 'single'),
      (2, 'double'),
      (3, 'suite'),
      (4, 'luxury'),
    )
    reservationID = models.AutoField(primary_key=True)
    checkin = models.DateField()
    checkout = models.DateField()
    adults = models.PositiveIntegerField()
    children = models.PositiveIntegerField()
    roomtype = models.PositiveSmallIntegerField(choices=ROOM_TYPE_CHOICES)
    rooms = models.PositiveIntegerField()
    email = models.EmailField(null=True)
    date_requested = models.DateTimeField(default=timezone.now)
    checkin_status = models.BooleanField(default=False)
    checkout_status = models.BooleanField(default=False)
