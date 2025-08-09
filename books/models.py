# Rebekah Reay - Student ID: K2938309
from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    cover = models.IntegerField()
    rating = models.CharField(max_length=255)
    review = models.CharField(max_length=255)
    swapspot = models.CharField(max_length=255)
    
