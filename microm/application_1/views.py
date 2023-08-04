# Create your views here.
# application_1/views.py

from django.shortcuts import render, redirect
from .forms import PrinterIPRequestForm
from .models import PrinterIPRequest

def request_printer_ip(request):
    if request.method == 'POST':
        form = PrinterIPRequestForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            form.save()
            # Render the 'thank_you.html' template after successful form submission
            return render(request, 'thank_you.html')
    else:
        form = PrinterIPRequestForm()

    return render(request, 'request_printer_ip.html', {'form': form})


