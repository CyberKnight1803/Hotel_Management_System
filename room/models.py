from django.db import models

# Create your models here.
class Room(models.Model):
    room_no = models.IntegerField()
    room_type = models.TextField(max_length=15) # Single, Double, Suite, Luxury
    status = models.TextField(max_length=10)  # occupied / Vacant
    email = models.EmailField(null=True) # Add this as foreign key to table.


