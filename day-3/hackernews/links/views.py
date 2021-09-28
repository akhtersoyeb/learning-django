from django.shortcuts import render
from .models import Link

def home(requests): 
    links_list = Link.objects.all()
    context = {
        "links_list": links_list
    }
    return render(requests, 'links/homepage.html', context)

def latest(requests): 
    links_list = Link.objects.all().order_by('-created_on')
    context = {
        "links_list": links_list
    }
    return render(requests, 'links/homepage.html', context)

def oldest(requests): 
    links_list = Link.objects.all().order_by('created_on')
    context = {
        "links_list": links_list
    }
    return render(requests, 'links/homepage.html', context)

def alphabetically(requests): 
    links_list = Link.objects.all().order_by('title')
    context = {
        "links_list": links_list
    }
    return render(requests, 'links/homepage.html', context)