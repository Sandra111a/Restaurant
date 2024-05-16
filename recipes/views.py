from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from .models import MenuItem
from forms import MenuItemForm


# Create your views here.

class RecipesView(View):
    """Widok zawiera menu restauracji."""
    def get(self, request):
        menu_items = MenuItem.objects.all()
        ctx = {
            'menu_items': menu_items,
        }
        return render(request, 'menu.html', ctx)


class AddMenuItemView(View):
    """Widok zawiera formularz zezwalający na wprowadzanie nowych pozycji do menu."""

    def get(self, request):
        form = MenuItemForm()
        ctx = {
            'form': form
        }
        return render(request, 'add_menu_item.html', ctx)

    def post(self, request):
        form = MenuItemForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Nowa pozycja została dodana do menu')
            return redirect('recipes')
        return render(request, 'add_menu_item.html', {'form': form})
