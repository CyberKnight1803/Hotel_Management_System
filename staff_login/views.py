from django.shortcuts import render

# Create your views here.
def register(request):
    return render(request, 'staff_login/login.html')

