from django.urls import path
from .views import BookListView, BookDetailView, BorrowBookView, ReturnBookView

app_name = 'library'

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:book_id>/', BookDetailView.as_view(), name='book-detail'),
    path('books/<int:book_id>/borrow/', BorrowBookView.as_view(), name='borrow-book'),
    path('books/<int:book_id>/return/', ReturnBookView.as_view(), name='return-book'),
]
