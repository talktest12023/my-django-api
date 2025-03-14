from django.contrib import admin
from .models import Post, Book

# Register your models here.

# admin.site.register(Post)  # Add Post model to admin panel


class BookAdmin(admin.ModelAdmin):
    # Show these columns in the admin list view
    list_display = ('id', 'title', 'author')
    search_fields = ('title', 'author')  # Allows searching by title or author
    list_filter = ('author',)  # Adds a filter sidebar for authors
    fieldsets = (
        ('Basic Info', {'fields': ('title', 'author')}),
    )
    readonly_fields = ('id',)  # Users cannot edit the ID


admin.site.register(Book, BookAdmin)  # Add Post model to admin panel
