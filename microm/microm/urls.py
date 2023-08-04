# my_project/urls.py
from django.contrib import admin
from django.urls import path, include  # Add 'include' here

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('application_1.urls')),  # Add this line to include your app's URLs
]
