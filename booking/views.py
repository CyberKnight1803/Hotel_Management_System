from django.shortcuts import render, redirect
from .forms import BookingForm
from django.contrib import messages
from .models import Reservation

from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
# Create your views here.

def bookings(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            
            """ details = {
                'checkin': form.cleaned_data.get('checkin'),
                'checkout': form.cleaned_data.get('checkout'),
                'roomtype': form.cleaned_data.get('roomtype'),
                'rooms': form._clean_fields.get('rooms'),
            }
            template = render_to_string('booking/email.html',)
            email = EmailMessage(
                'Reservation Confirmation #', 
                template,
                settings.EMAIL_HOST_USER,
                
            )
            email.fail_silently=False
            email.send() """
            messages.success(request, f'Booking Queued')
            return redirect('Customer_Home')

        """ checkin = form.cleaned_data['checkin']
        checkout = form.cleaned_data['checkout']
        adults = form.cleaned_data['adults']
        children = form.cleaned_data['children']
        roomtype = form.cleaned_data['roomtype']
        rooms = form.cleaned_data['rooms']

        booking = Bookings(checkin=checkin, checkout=checkout, adults=adults, children=children,
        roomtype=roomtype,rooms=rooms)
        booking.save() """
    else:
        form = BookingForm()

    return render(request, 'booking/base.html', {'form' : form})
