from django.db import models
from django.contrib.auth.models import User


STATE_CHOICES = (
    ('Bengal','Bengal'), 
    ('California','California'), 
    ('Texas','Texas'),
    ('state 4', 'state 4')
)

class Resume(models.Model): 
    name = models.CharField(max_length=150)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    gender = models.CharField(max_length=30)
    locality = models.CharField(max_length=150)
    state = models.CharField(max_length=150, choices=STATE_CHOICES)
    profile_image = models.ImageField(upload_to='profile_images/')
    doc_file = models.FileField(upload_to='extra_files/')
