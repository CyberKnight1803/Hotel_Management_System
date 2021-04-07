from django import forms
from .models import Reservation

class BookingForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['checkin', 'checkout', 'adults', 'children', 'roomtype', 'rooms']
