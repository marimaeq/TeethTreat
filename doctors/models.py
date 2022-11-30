from django.db import models


class Doctor(models.Model):
    speciality = models.CharField(max_length=20)
    name = models.CharField(max_length=15)
    
    # availableHours = models.
    # photo