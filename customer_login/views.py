
from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

# Imports necessary for Email 
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            user_email = form.cleaned_data.get('email')

            template = render_to_string('customer_login/email.html', {'name': username})
            email = EmailMessage(
                'New Account!',
                template,
                settings.EMAIL_HOST_USER,
                [user_email]
            )
            email.fail_silently=False
            email.send()
            messages.success(request, f'Account created for {username}. You can now login')
            return redirect('Customer_Home')
    else:
        form = UserRegisterForm()
    return render(request, 'customer_login/register.html', {'form': form})

@login_required  # decorator
def profile(request):
    return render(request, 'customer_login/profile.html')
