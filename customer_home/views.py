from django.shortcuts import render

def home(request):
    return render(request, 'customer_home/customer_home.html')

def customerHomeRooms(request):
    return render(request, 'customer_home/new_rooms.html')