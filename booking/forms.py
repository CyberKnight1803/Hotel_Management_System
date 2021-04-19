from django import forms
from .models import Reservation, Feedback

class BookingForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['checkin', 'checkout', 'adults', 'children', 'roomtype', 'rooms']

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7']

