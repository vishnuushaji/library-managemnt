from django.contrib import admin
from django.urls import include, path
from library.views import BookListView, BookDetailView, BorrowBookView, ReturnBookView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('library/', include('library.urls')),
    path('', BookListView.as_view(), name='book-list'),  
    path('books/<int:book_id>/', BookDetailView.as_view(), name='book-detail'),
    path('books/<int:book_id>/borrow/', BorrowBookView.as_view(), name='borrow-book'),
    path('books/<int:book_id>/return/', ReturnBookView.as_view(), name='return-book'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
