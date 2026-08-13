from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('aboutus/', views.about, name='aboutus'),
    path('services/', views.services, name='services'),
    path('contactus/', views.contact, name='contactus'),
]