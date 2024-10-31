import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from .models import HallUser

@pytest.mark.django_db
def test_user_login(client):
    user = HallUser.objects.create_user(email='test@example.com', password='password123')
    response = client.post(reverse('login'), {'email': 'test@example.com', 'password': 'password123'})
    assert response.status_code == status.HTTP_200_OK
    assert 'token' in response.data

@pytest.mark.django_db
def test_hall_user_creation(client):
    client.login(email='test@example.com', password='password123')
    response = client.post(reverse('user-list-create'), {'email': 'newuser@example.com', 'password': 'password123'})
    assert response.status_code == status.HTTP_201_CREATED
    assert HallUser.objects.filter(email='newuser@example.com').exists()
