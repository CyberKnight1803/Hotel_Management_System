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
            #form.save()
            reservationID = form.cleaned_data.get('reservationID')
            user_email = request.user.email
            username = request.user.username
            checkin = form.cleaned_data['checkin']
            checkout = form.cleaned_data['checkout']
            adults = form.cleaned_data['adults']
            children = form.cleaned_data['children']
            roomtype = form.cleaned_data['roomtype']
            rooms = form.cleaned_data['rooms']

            booking = Reservation(checkin=checkin, checkout=checkout, adults=adults, children=children,
            roomtype=roomtype,rooms=rooms, email=user_email)
            booking.save()
            time = booking.date_requested
            B = Reservation.objects.raw('SELECT "reservationID" FROM booking_reservation WHERE "email"=%s and "date_requested"=%s', [user_email, time])
            details = {
                'name': username,
                'checkin': checkin,
                'checkout': checkout,
                'roomtype': roomtype,
                'rooms': rooms,
            }
            template = render_to_string('booking/email.html', details)
            email = EmailMessage(
                'Reservation Confirmation #' + str(B[0].reservationID), 
                template,
                settings.EMAIL_HOST_USER,
                [user_email]
            )
            email.fail_silently=False
            email.send()
            messages.success(request, f'Booking Queued')
            return redirect('Customer_Home')
    else:
        form = BookingForm()

    return render(request, 'booking/base.html', {'form' : form})
