from django.urls import path
from staff_home import views as home_views

urlpatterns = [
    path('home/', home_views.home, name='home')
]
