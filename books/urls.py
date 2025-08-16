# Rebekah Reay - Student ID: K2938309
from django.urls import path
from . import views

urlpatterns = [
    path('all_books/', views.all_books, name='all_books'),
    path('all_books/book_details/<str:title>/', views.book_details, name='book_details'),
    path('all/', views.get_books_api, name='get_books_api'),
    path('create/', views.create_book, name='create_book'),
    path('update_reservation/', views.update_book_reservation, name='update_reservation')
]