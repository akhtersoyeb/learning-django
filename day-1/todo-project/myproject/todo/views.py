# from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(requests): 
    return HttpResponse("Congrats")

def about(requests): 
    return HttpResponse("About page")

# add in root urls.py file -> app/urls.py -> app.views.py