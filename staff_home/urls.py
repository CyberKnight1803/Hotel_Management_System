from django.urls import path
from staff_home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('detail/', views.detail, name='detailview')
]
