"""
URL configuration for restaurant project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from clients.views import LoginView, RegistrationView
from recipes.views import AddMenuItemView, RecipesView, IngredientView
from orders.views import OrderView, ReservationView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='login'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('recipes/', RecipesView.as_view(), name='recipes'),
    path('add_menu_item/', AddMenuItemView.as_view(), name='add_menu_item'),
    path('place_order/', OrderView, name='place_order'),
    path('reservation/', ReservationView, name='reservation'),
    path('ingredients/', IngredientView, name='ingredients'),

]
