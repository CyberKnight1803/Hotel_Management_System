from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['checkin', 'checkout', 'adults', 'children', 'roomtype', 'rooms']
