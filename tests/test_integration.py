import pytest
from django.urls import reverse
from rest_framework import status
from .models import HallUser

@pytest.mark.django_db
def test_login_and_update_profile(client):
    user = HallUser.objects.create_user(email='test@example.com', password='password123')
    login_response = client.post(reverse('login'), {'email': 'test@example.com', 'password': 'password123'})
    token = login_response.data['token']

    client.credentials(HTTP_AUTHORIZATION='Token ' + token)
    update_response = client.patch(reverse('update-profile'), {'first_name': 'NewName'})
    assert update_response.status_code == status.HTTP_200_OK
    user.refresh_from_db()
    assert user.first_name == 'NewName'
