from django.db import models


class Doctor(models.Model):
    speciality = models.CharField(max_length=20, null=True, blank=True)
    name = models.CharField(max_length=15)
    photo = models.ImageField(upload_to='', null=True, blank=True)
    
    # availableHours = models.
    # MEDIA_ROOT/upload_to