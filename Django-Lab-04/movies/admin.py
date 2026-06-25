from django.contrib import admin
from .models import Category, Cast, Movie, Series

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Cast)
class CastAdmin(admin.ModelAdmin):
    list_display = ('name', 'role')
    search_fields = ('name', 'role')
    list_filter = ('role',)

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'duration_minutes')
    search_fields = ('title', 'description')
    list_filter = ('release_date', 'categories')

@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'seasons_count')
    search_fields = ('title', 'description')
    list_filter = ('release_date', 'categories')
