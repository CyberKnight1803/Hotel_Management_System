from django.shortcuts import render
from booking.models import Reservation

def home(request):
    reservations = Reservation.objects.all()
    return render(request, 'staff_home/base.html', {'reservations': reservations})

def detail(request):
    reservation = Reservation.objects.filter(reservationID=3).first()
    return render(request, 'staff_home/detail.html', {'reservation': reservation})
