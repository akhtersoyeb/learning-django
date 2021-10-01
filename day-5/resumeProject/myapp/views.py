from django.http.response import HttpResponse
from django.shortcuts import render, redirect

from .models import Resume 
from .forms  import ResumeForm

def home(requests): 
    if requests.method == 'POST': 
        if requests.user.is_authenticated : 
            form = ResumeForm(requests.POST, requests.FILES)
            if form.is_valid() :
                form.save() 
                context = {
                    'form': form
                }
                return render(requests, 'myapp/home.html', context )
        else : 
            return HttpResponse("You are not allowed to add data")

    resume_list = Resume.objects.all() 
    form = ResumeForm()
    context = {
        'resume_list': resume_list,
        'form': form, 
    }
    return render(requests, 'myapp/home.html', context)

def resume(requests, pk): 
    resume = Resume.objects.get(id=pk)
    context = {
        'resume': resume
    }

    return render(requests, 'myapp/resumeView.html', context)