from django.db import models

# Create your models here.
class Category(models.Model):
  category_name = models.CharField(max_length=50, unique=True)
  crated_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)