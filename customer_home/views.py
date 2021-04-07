from django.shortcuts import render

def home(request):
    return render(request, 'customer_home/customer_home.html')
