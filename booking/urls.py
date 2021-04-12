from django.urls import path
from . import views

urlpatterns = [
    path('', views.bookings, name='Booking'),
    path('grid/', views.grid_view, name='grid')
]
