# application_1/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.request_printer_ip, name='request_printer_ip'),
    # Other URL patterns for other views can be added here
]
