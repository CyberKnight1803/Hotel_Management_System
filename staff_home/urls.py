from django.urls import path
from staff_home import views
from booking import views as booking_views

urlpatterns = [
    path('', views.home, name='home'),
    path('detail/<int:pk>/', views.detail.as_view(), name='detailview'),
    path('rooms/', booking_views.grid_view),
    path('availability/', views.availability)
]
