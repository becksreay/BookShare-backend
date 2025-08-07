from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    cover = models.IntegerField(max_length=255)
    rating = models.CharField(max_length=255)
    review = models.CharField(max_length=255)
    swapspot = models.CharField(max_length=255)
    
