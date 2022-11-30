from django.shortcuts import render
from django.http import HttpResponse


def home_view(requres, *args, **kwargs):
    return HttpResponse('currently no doctors:(')