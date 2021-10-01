from django.shortcuts import render

def homeView(requests): 
    return render(requests, 'pages/home.html')
