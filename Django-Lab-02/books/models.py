from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField(blank=True, null=True)
    rate = models.PositiveIntegerField(default=0)
    views = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
