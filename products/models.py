from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=140)
    nutrition_grade = models.CharField(max_length=1)
    url = models.CharField(max_length=255)
    categories = models.ManyToManyField("Category", related_name="products")

    def __str__(self):
        return self.titre

class Category(models.Model):
    name = models.CharField(max_length=140)
    
    def __str__(self):
        return self.titre

