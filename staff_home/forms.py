from django import forms
from django.conf import settings

class DateInput(forms.DateInput):
    input_type = 'date'

class AvailabilityForm(forms.Form):
    date = forms.DateField(widget=DateInput, input_formats=['%Y-%m-%d'])
    
                               