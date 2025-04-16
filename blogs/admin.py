# admin.py
from django.contrib import admin
from .models import Category

class CategoryAdmin(admin.ModelAdmin):
  list_display = ('id', 'category_name', 'created_at', 'updated_at')

admin.site.register(Category, CategoryAdmin)