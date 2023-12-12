from django.db import models

class Movie(models.Model):
    name=models.CharField(max_length=100,default="")
    image=models.CharField(max_length=100,default="")
    actor=models.CharField(max_length=100,default="")
    actress=models.CharField(max_length=100,default="")
    director=models.CharField(max_length=100,default="")
    producer=models.CharField(max_length=100,default="")
# Create your models here.
