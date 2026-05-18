from django.contrib import admin

from .models import Category, Blog

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title', 'Category', 'author', 'status', 'is_featured',]
    search_fields = ['title', 'Category__Category_name', 'author__username']
    list_filter = ['status', 'is_featured', 'created_at']
    list_editable = ['is_featured']

admin.site.register(Category)
admin.site.register(Blog, BlogAdmin) 