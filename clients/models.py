from django import forms
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# class Client(models.Model):
#     username = models.CharField(max_length=30, unique=True)
#     password1 = models.CharField(max_length=30, unique=True)
#     email = models.EmailField(unique=True)


class MyUser(User):
    pass


