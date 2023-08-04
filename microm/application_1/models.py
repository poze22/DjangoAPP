# Create your models here.
from django.db import models


class PrinterIPRequest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    reason = models.TextField()
    status = models.CharField(max_length=50, default='Pending')

    def __str__(self):
        return f"{self.name} - {self.status}"
