import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from django.test import RequestFactory
from django.urls import reverse
from recipes.models import Ingredient
from recipes.views import IngredientView


@pytest.mark.django_db
def test_menu_view(client):
    response = client.get(reverse('recipes'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_ingredient_view(client):
    user = User.objects.create_user(username='testuser', password='12345')
    client.login(username='testuser', password='12345')
    request_factory = RequestFactory()
    request = request_factory.get(reverse('ingredients'))
    request.user = user
    view = IngredientView
    response = view(request)
    assert response.status_code == 200
