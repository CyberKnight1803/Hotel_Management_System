from django.shortcuts import render, redirect
from .forms import BookingForm
from .models import Bookings
# Create your views here.

def bookings(request):
    if request.method == 'POST':
        form = BookingForm(request.method)
        if form.is_valid():
            form.save()
            """ checkin = form.cleaned_data['checkin']
            checkout = form.cleaned_data['checkout']
            adults = form.cleaned_data['adults']
            children = form.cleaned_data['children']
            roomtype = form.cleaned_data['roomtype']
            rooms = form.cleaned_data['rooms']

            booking = Bookings(checkin=checkin, checkout=checkout, adults=adults, children=children,
            roomtype=roomtype,rooms=rooms)
            booking.save() """
            return redirect('http://127.0.0.1:8000/')
                    
    return render(request, 'booking/base.html', {'form' : BookingForm()})