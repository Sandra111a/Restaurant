import pytest
from django.urls import reverse
from recipes.models import Ingredient
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_menu_view(client):
    response = client.get(reverse('recipes'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_ingredient_view(client):
    user = User.objects.create_user(username='testuser', password='12345')
    client.login(username='testuser', password='12345')
    response = client.get(reverse('ingredients'))
    assert response.status_code == 200

