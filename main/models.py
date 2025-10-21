from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=100, unique=True)
    def __str__(self):
        return self.title


