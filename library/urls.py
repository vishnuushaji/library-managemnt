from django.urls import path
from .views import book_list, book_detail, borrow_book, return_book

urlpatterns = [
    path('books/', book_list, name='book_list'),
    path('books/<int:book_id>/', book_detail, name='book_detail'),
    path('books/<int:book_id>/borrow/', borrow_book, name='borrow_book'),
    path('books/<int:book_id>/return/', return_book, name='return_book'),
]
