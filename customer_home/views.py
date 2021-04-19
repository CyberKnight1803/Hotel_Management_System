from django.shortcuts import render
from .utils import rList
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'customer_home/customer_home.html')

def customerHomeRooms(request):
    return render(request, 'customer_home/new_rooms.html')

@login_required
def customerBookingHistory(request):
    email = request.user.email
    bookings = rList(email)
    context = {
        'bookings': bookings,
    }
    return render(request, 'customer_home/customerHistory.html', context)
