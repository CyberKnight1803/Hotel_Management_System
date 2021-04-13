from django import forms
from .models import Reservation

class BookingForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['checkin', 'checkout', 'adults', 'children', 'roomtype', 'rooms']

    checkin = forms.DateField(
        widget=forms.DateInput(format='%d-%m-%Y'),
        input_formats=('%d/%m/%Y', )
    )
    checkout = forms.DateField(
        widget=forms.DateInput(format='%d-%m-%Y'),
        input_formats=('%d-%m-%Y', )
    )