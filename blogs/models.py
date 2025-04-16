# models.py
from django.db import models

class Category(models.Model):
  category_name = models.CharField(max_length=50, unique=True)
  created_at = models.DateTimeField(auto_now_add=True)  # fixed typo here
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    verbose_name_plural = 'Categories'
