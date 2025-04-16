# admin.py
from django.contrib import admin
from .models import Category,Blogs

class CategoryAdmin(admin.ModelAdmin):
  list_display = ('id', 'category_name', 'created_at', 'updated_at')
  
class BlogAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'slug', 'category', 'author', 'blog_image', 'short_description', 'blogs_body', 'status', 'is_featured', 'created_at', 'updated_at')
  pre_populated_fields = {'slug': ('title',)}
  search_fields = ('id', 'title', 'category__category_name', 'status')
  list_editable = ('is_featured',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Blogs, BlogAdmin)