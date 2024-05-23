from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=1)


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    categories = models.ManyToManyField(Category)
    ingredients = models.ManyToManyField(Ingredient)
