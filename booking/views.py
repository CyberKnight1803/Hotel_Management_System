from django.shortcuts import render, redirect
from .forms import BookingForm
from django.contrib import messages
from .models import Reservation
# Create your views here.

def bookings(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
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
