from django.db import models

class Person(models.Model):
    nom= models.CharField(max_length=100)
    prenom= models.CharField(max_length=100)
    role=models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)
    updated = models.DateTimeField(auto_now=True, blank=True)
    image = models.ImageField(upload_to ='uploads/')