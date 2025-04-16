# models.py
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
  category_name = models.CharField(max_length=50, unique=True)
  created_at = models.DateTimeField(auto_now_add=True)  # fixed typo here
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    verbose_name_plural = 'Categories'
    

STATUS_CHOICE = (
    ('draft', 'Draft'),
    ('public', 'Published'),
)    

class Blogs(models.Model):
  title = models.CharField(max_length=100, unique=True)
  slug = models.SlugField(unique=True, blank=True)
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  blog_image = models.ImageField(upload_to='uploads/%y/%m/%d')
  short_description = models.TextField(max_length=2000)
  blogs_body = models.TextField(max_length=5000)
  status = models.IntegerField(choices = STATUS_CHOICE, default='draft')
  is_featured = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  class Meta:
    verbose_name_plural = 'Blogs'