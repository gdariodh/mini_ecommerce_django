from django.contrib import admin
from categories.models import Category

@admin.register(Category)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created_at', 'published')
