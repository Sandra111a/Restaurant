from django.db import models
from django.contrib.auth.models import User
from clients.models import MyUser
from django.apps import apps
from recipes.models import MenuItem


# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, default=1)
    date = models.DateTimeField(auto_now_add=True)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def save(self, *args, **kwargs):
        MenuItem = apps.get_model('recipes', 'MenuItem')
        super().save(*args, **kwargs)


class Table(models.Model):
    number = models.PositiveIntegerField(unique=True)
    seats = models.PositiveIntegerField()


class Reservation(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    customer_name = models.CharField(max_length=100)
    order = models.OneToOneField(Order, on_delete=models.SET_NULL, null=True, blank=True)
