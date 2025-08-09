# Rebekah Reay - Student ID: K2938309
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def landing_page(request):
    return render(request, "landing.html")
   