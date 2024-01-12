from django.contrib import admin
from django.urls import include, path
from library.views import book_list
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('library/', include('library.urls')),
     path('', book_list, name='home'), 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)