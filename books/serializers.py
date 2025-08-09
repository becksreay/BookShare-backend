# Rebekah Reay - Student ID: K2938309
from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'cover', 'rating', 'review', 'swapspot']