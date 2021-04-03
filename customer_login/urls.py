from django.urls import path
from customer_login import views as login_views

urlpatterns = [
    path('', login_views.register, name='SignUp')
]
