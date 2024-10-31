import pytest
from django.urls import reverse
from rest_framework import status
from .models import HallUser

@pytest.mark.django_db
def test_hall_user_creation():
    user = HallUser.objects.create_user(email='test@example.com', password='password123')
    assert user.email == 'test@example.com'
    assert user.check_password('password123')
