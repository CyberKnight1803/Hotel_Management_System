from django.urls import path
from staff_login import views as staff_login_views
from staff_home import views as staff_home_views

urlpatterns = [
    path('', staff_login_views.loginPage, name='SignUp'),
    path('home/', staff_home_views.home, name='home')
]
