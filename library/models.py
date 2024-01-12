from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField()
    borrowed = models.BooleanField(default=False)
    image = models.ImageField(upload_to='book_images/', blank=True, null=True)

    def __str__(self):
        return self.title