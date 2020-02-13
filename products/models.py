from django.db import models

from .managers import ProductManager


class Product(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=140)
    nutrition_grade = models.CharField(max_length=1)
    url = models.CharField(max_length=255)
    image_url = models.URLField(max_length=255)
    image_nutrition_url = models.URLField(max_length=255)
    objects = ProductManager()
    categories = models.ManyToManyField("Category", related_name="products")

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=140)
    
    def __str__(self):
        return self.name




