from django.urls import path
from staff_login import views as staff_login_views

urlpatterns = [
    path('', staff_login_views.register, name='SignUp')
]
