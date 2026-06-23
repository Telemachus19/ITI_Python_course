from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def clean(self):
        super().clean()
        if self.name:
            name_len = len(self.name.strip())
            if name_len < 2:
                raise ValidationError({'name': 'The minimum length of a category name is 2 characters.'})

    def __str__(self):
        return self.name

class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books')
    categories = models.ManyToManyField(Category, related_name='books')
    title = models.CharField(max_length=200)
    desc = models.TextField(blank=True, null=True)
    rate = models.PositiveIntegerField(default=0)
    views = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        super().clean()
        if self.title:
            title_len = len(self.title.strip())
            if title_len < 10 or title_len > 50:
                raise ValidationError({'title': 'The length of a book title must be between 10 and 50 characters.'})

    def __str__(self):
        return self.title

class ISBN(models.Model):
    book = models.OneToOneField(Book, on_delete=models.CASCADE, related_name='isbn')
    author_title = models.CharField(max_length=200)
    book_title = models.CharField(max_length=200)
    isbn_number = models.CharField(max_length=13, unique=True, blank=True)

    def __str__(self):
        return f"{self.book_title} - {self.isbn_number}"

