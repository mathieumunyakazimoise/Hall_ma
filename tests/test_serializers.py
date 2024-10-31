import pytest
from .serializers import HallUserListCreateSerializer
from .models import HallUser

@pytest.mark.django_db
def test_hall_user_serializer():
    data = {
        'email': 'test@example.com',
        'password': 'password123',
        'confirm_password': 'password123',
    }
    serializer = HallUserListCreateSerializer(data=data)
    assert serializer.is_valid()
    user = serializer.save()
    assert user.email == 'test@example.com'
