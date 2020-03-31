from django.db import models

class Blog(models.model):
    summary = models.CharField (max_length= 2000)
    images = models.ImageField (upload_to= 'images/')
