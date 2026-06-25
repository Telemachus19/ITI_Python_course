from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Cast(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        if self.role:
            return f"{self.name} ({self.role})"
        return self.name

class MediaContent(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    release_date = models.DateField()
    categories = models.ManyToManyField(Category, related_name='%(class)s_contents')
    casts = models.ManyToManyField(Cast, related_name='%(class)s_contents')
    poster_image = models.ImageField(upload_to='posters/', blank=True, null=True)

    class Meta:
        abstract = True

class Movie(MediaContent):
    duration_minutes = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.title

class Series(MediaContent):
    seasons_count = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.title
