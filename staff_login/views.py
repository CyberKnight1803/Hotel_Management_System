from django.core.checks import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from staff_login.models import StaffLogin

# Create your views here.
def loginPage(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = StaffLogin.objects.raw('select * from staff_login_stafflogin where "Email" = %s and "Password" = %s', [email, password])
        if len(user) == 1:
            return redirect('home')
        else:
            messages.info(request, 'Email or Password is incorrect')

    return render(request, 'staff_login/login.html')