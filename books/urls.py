# Rebekah Reay - Student ID: K2938309
from django.urls import path
from . import views

urlpatterns = [
    path('', views.allbooks, name='books'),
    path('all/', views.get_books, name='get_all_books'),
    path('create/', views.create_book, name='create_book'),
    path('update_reservation/', views.update_book_reservation, name='update_reservation')
]