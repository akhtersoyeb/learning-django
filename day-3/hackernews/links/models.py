from django.db import models

# title 
# description
# url link
# authors name
# date of creation

class Link(models.Model): 
    title = models.CharField(max_length=150)
    description = models.TextField() 
    url = models.URLField(max_length=150)
    author = models.CharField(max_length=50)
    created_on = models.DateTimeField(auto_now_add=True)

