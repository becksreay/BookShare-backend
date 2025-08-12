# Rebekah Reay - Student ID: K2938309
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import BookSerializer
from .models import Book

# Create your views here.
def allbooks(request):
    mybooks = Book.objects.all().values()
    template = loader.get_template('all_books.html')
    context = {
       'mybooks': mybooks,
    }
    return HttpResponse(template.render(context, request))

@api_view(['GET'])
def get_books(request):
    books = Book.objects.all()

    title = request.GET.get('title')
    if title:
        books = books.filter(title__icontains=title)

    author = request.GET.get('author')
    if author:
        books = books.filter(author__icontains=author)

    swapspot = request.GET.get('swapspot')
    if swapspot:
        books = books.filter(swapspot__icontains=swapspot)
    
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_book(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['PATCH'])
def update_book_reservation(request):
    title = request.data.get("title")
    if not title:
        return Response({"error": "Missing 'title' field"}, status=status.HTTP_400_BAD_REQUEST)
    try:
        book = Book.objects.get(title=title)
    except Book.DoesNotExist:
        return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)

    new_reservation = request.data.get("reservedBy")
    if new_reservation is None:
        return Response({"error": "Missing 'reservedBy' field"}, status=status.HTTP_400_BAD_REQUEST)
    
    book.reservedBy = new_reservation
    book.save()

    return Response({"message": "ReservedBy updated successfully", "reservedBy": book.reservedBy})