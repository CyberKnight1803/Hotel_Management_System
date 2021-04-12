from django.urls import path
from staff_home import views
from booking import views as booking_views

urlpatterns = [
    path('', views.home, name='home'),
    path('detail/', views.detail, name='detailview'),
    path('rooms/', booking_views.grid_view)
]
