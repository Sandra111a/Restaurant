import pytest
from django.urls import reverse
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_order_view(client):
    user = User.objects.create_user(username='testuser', password='12345')
    client.login(username='testuser', password='12345')
    response = client.get(reverse('place_order'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_reservation_view(client):
    user = User.objects.create_user(username='testuser', password='12345')
    client.login(username='testuser', password='12345')
    response = client.get(reverse('reservation'))
    assert response.status_code == 200