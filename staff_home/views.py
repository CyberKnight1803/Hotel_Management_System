from django.shortcuts import render
from booking.models import Reservation
from users.decorators import staff_required
from django.contrib.auth.decorators import login_required


@login_required
@staff_required
def home(request):
    reservations = Reservation.objects.all()
    return render(request, 'staff_home/base.html', {'reservations': reservations})


@login_required
@staff_required
def detail(request):
    reservation = Reservation.objects.filter(reservationID=3).first()
    return render(request, 'staff_home/detail.html', {'reservation': reservation})
