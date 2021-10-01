
from django.urls import path 
from . import views 

urlpatterns = [ 
    path('', views.home, name='homeUrl'),
    path('<int:pk>/view/', views.resume, name='resumeUrl')
]