from django.shortcuts import render, get_object_or_404 , redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Book
from .forms import BorrowForm

class BookListView(ListView):
    model = Book
    template_name = 'library/book_list.html'
    context_object_name = 'books'

class BookDetailView(DetailView):
    model = Book
    template_name = 'library/book_detail.html'
    context_object_name = 'book'
    pk_url_kwarg = 'book_id'

class BorrowBookView(View):
    template_name = 'library/borrow_book.html'

    def post(self, request, book_id):
        book = get_object_or_404(Book, pk=book_id)

        if not book.borrowed:
            book.borrowed = True
            book.save()

        return redirect(reverse('book-list'))

class ReturnBookView(View):
    template_name = 'library/return_book.html'

    def post(self, request, book_id):
        book = get_object_or_404(Book, pk=book_id)

        if book.borrowed:
            book.borrowed = False
            book.save()

        return redirect(reverse('book-list'))