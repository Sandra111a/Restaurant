from django import forms
from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class MyUser(User):
    is_staff_member = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=True)

