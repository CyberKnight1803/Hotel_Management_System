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


class Feedback(models.Model):
  FEEDBACK_CHOICES = (
    (1, 'Very Satisfied'),
    (2, 'Satisfied'),
    (3, 'Unsatisfied'),
  )
  q1 = models.PositiveSmallIntegerField(choices=FEEDBACK_CHOICES)
  q2 = models.PositiveSmallIntegerField(choices=FEEDBACK_CHOICES)
  q3 = models.PositiveSmallIntegerField(choices=FEEDBACK_CHOICES)
  q4 = models.PositiveSmallIntegerField(choices=FEEDBACK_CHOICES)
  q5 = models.PositiveSmallIntegerField(choices=FEEDBACK_CHOICES)
  q6 = models.PositiveSmallIntegerField(choices=FEEDBACK_CHOICES)
  q7 = models.PositiveSmallIntegerField(choices=FEEDBACK_CHOICES)

