# application_1/forms.py
from django import forms
from .models import PrinterIPRequest


class PrinterIPRequestForm(forms.ModelForm):
    class Meta:
        model = PrinterIPRequest
        fields = ['name', 'email', 'reason']
