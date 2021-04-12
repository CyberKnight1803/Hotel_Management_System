from django.contrib import messages
from .forms import StaffSignUpForm, CustomerSignUpForm
from django.views.generic import CreateView
from .models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .decorators import staff_required
from django.utils.decorators import method_decorator

# Imports necessary for Email
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string


@method_decorator([login_required, staff_required], name='dispatch')
class StaffSignUpView(CreateView):
    model = User
    form_class = StaffSignUpForm
    template_name = 'users/register.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'staff'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        # username = form.cleaned_data.get('username')
        # user_email = form.cleaned_data.get('email')

        # template = render_to_string('customer_login/email.html', {'name': username})
        # email = EmailMessage(
        #     'New Account!',
        #     template,
        #     settings.EMAIL_HOST_USER,
        #     [user_email]
        # )
        # email.fail_silently=False
        # email.send()
        # messages.success(request, f'Account created for {username}. You can now login')
        return redirect('home')


class CustomerSignUpView(CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name = 'users/register.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'customer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        # username = form.cleaned_data.get('username')
        # user_email = form.cleaned_data.get('email')

        # template = render_to_string('customer_login/email.html', {'name': username})
        # email = EmailMessage(
        #     'New Account!',
        #     template,
        #     settings.EMAIL_HOST_USER,
        #     [user_email]
        # )
        # email.fail_silently=False
        # email.send()
        # messages.success(request, f'Account created for {username}. You can now login')
        return redirect('home')


@login_required
def profile(request):
    return render(request, 'users/profile.html')