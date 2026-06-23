from django.contrib import admin
from .models import Book, Category, ISBN

class ISBNInline(admin.StackedInline):
    model = ISBN
    can_delete = False
    verbose_name_plural = 'ISBN Information'

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'rate', 'views', 'created_at', 'get_categories')
    list_filter = ('categories', 'user', 'rate', 'created_at')
    search_fields = ('title', 'desc', 'user__username')
    inlines = [ISBNInline]

    def get_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all()])
    get_categories.short_description = 'Categories'

