from django.shortcuts import render
from django.http import HttpResponse

from .models import Doctor


def home_view(request, *args, **kwargs):
    return HttpResponse('currently no doctors:(')


def doctors_list(request, *args, **kwargs):
    doctors = Doctor.objects.all()
    context = {
        'doctors': doctors
    }
    return render(request, 'doctors/index.html', context)