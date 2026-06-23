from django.db.models.signals import post_save
from django.dispatch import receiver
import random
from .models import Book, ISBN

@receiver(post_save, sender=Book)
def create_book_isbn(sender, instance, created, **kwargs):
    if created:
        # Generate a random 13-digit ISBN number
        isbn_num = "".join([str(random.randint(0, 9)) for _ in range(13)])
        # Author title is instance.user's name or username
        author = instance.user.username if instance.user else "Unknown Author"
        ISBN.objects.create(
            book=instance,
            author_title=author,
            book_title=instance.title,
            isbn_number=isbn_num
        )
