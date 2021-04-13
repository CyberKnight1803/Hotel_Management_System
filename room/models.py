from django.db import models
from booking.models import Reservation

# Create your models here.
class Room(models.Model):
    room_no = models.IntegerField(primary_key=True)
    room_type = models.TextField(max_length=15) # Single, Double, Suite, Luxury
    status = models.TextField(max_length=10)  # occupied / Vacant
    reservationID = models.ForeignKey(Reservation, on_delete=models.CASCADE, null=True)

