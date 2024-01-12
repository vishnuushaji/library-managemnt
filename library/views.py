# library/views.py
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Book
from .forms import BookForm, BorrowForm

def book_list(request):
    books = Book.objects.all()
    return render(request, 'library/book_list.html', {'books': books})

def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'library/book_detail.html', {'book': book})

def borrow_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)

    if request.method == 'POST':
        form = BorrowForm(request.POST)
        if form.is_valid():
            borrower_name = form.cleaned_data['borrower_name']
            borrower_email = form.cleaned_data['borrower_email']

            if not book.borrowed:
                book.borrowed = True
                book.save()
                return HttpResponseRedirect('/library/books/') 
    else:
        form = BorrowForm()

    return render(request, 'library/borrow_book.html', {'book': book, 'form': form})
def return_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)

    if book.borrowed:
        book.borrowed = False
        book.save()
    return render(request, 'library/return_book.html', {'book_id': book_id})
