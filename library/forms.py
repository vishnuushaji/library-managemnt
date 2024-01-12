from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description', 'image']

class BorrowForm(forms.Form):
    borrower_name = forms.CharField(max_length=100)
    borrower_email = forms.EmailField()
