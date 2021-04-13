from django.shortcuts import render
from booking.models import Reservation
from users.decorators import staff_required
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import DetailView

@login_required
@staff_required
def home(request):
    reservations = Reservation.objects.raw('SELECT * FROM booking_reservation')
    return render(request, 'staff_home/base.html', {'reservations': reservations})


# @login_required
# @staff_required
# def detail(request):
#     reservation = Reservation.objects.filter(reservationID=3).first()
#     return render(request, 'staff_home/detail.html', {'reservation': reservation})


# @method_decorator([login_required, staff_required], name='dispatch')
# class detail():
#     model = Reservation
#     template_name = 'staff_home/base.html'

#     def get_object(self, queryset=None):
#         return Ticket.objects.get(pk=self.kwargs.get("pk"))

# @method_decorator([login_required, staff_required], name='dispatch')
class detail(DetailView):
    model = Reservation
    template_name = 'staff_home/detail.html'
