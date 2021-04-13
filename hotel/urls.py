"""hotel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from users import views as login_views
# from customer_login import views as customer_login_views
# from customer_home import views as customer_home_views
# from booking import views as booking_views

urlpatterns = [
    # path('register/', include('customer_login.urls')),
    # path('login/', auth_views.LoginView.as_view(template_name='customer_login/login.html'), name='login'),
    path('admin/', admin.site.urls),
    path('accounts/signup/customer/', login_views.CustomerSignUpView.as_view(), name='register'),
    path('accounts/signup/staff/', login_views.StaffSignUpView.as_view(), name='register_staff'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', login_views.profile, name='profile'),
    # path('stafflogin/', include('staff_login.urls')),
    path('staff_home/', include('staff_home.urls')),
    path('', include('customer_home.urls')),
    path('booking/', include('booking.urls')),
]
