from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from recipes.models import MenuItem
from orders.models import OrderItem


class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1']


class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ['name', 'description', 'price']


class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['menu_item', 'quantity']

