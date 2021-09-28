from django.urls import path 
from . import views

urlpatterns = [ 
    path('', views.home, name='homeUrl'),
    path('latest/', views.latest, name='latestLinks'), 
    path('oldest/', views.oldest, name='oldestLink'), 
    path('alphabetically/', views.alphabetically, name='alphabeticallyLinks')
]