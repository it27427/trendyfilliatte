from django.contrib import admin
from . models import Category

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
  list_display = ('id', 'category_name', 'created_at', 'updated_at')

admin.site.register(Category)
