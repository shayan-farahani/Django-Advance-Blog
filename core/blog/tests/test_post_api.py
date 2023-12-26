from rest_framework.test import APIClient
from django.urls import reverse
import pytest
from datetime import datetime
from accounts.models import User


@pytest.fixture
def api_client():
    client = APIClient()
    return client


@pytest.fixture
def common_user():
    user = User.objects.create_user(
        email="admin@admin.com", password="a/@1234567", is_verified=True
    )
    return user


@pytest.mark.django_db
class TestPostApi:
    def test_get_post_response_200_status(self, api_client):
        url = reverse("blog:api-v1:post-list")
        response = api_client.get(url)
        assert response.status_code == 200

    def test_create_post_response_401_status(self, api_client):
        url = reverse("blog:api-v1:post-list")
        data = {
            "title": "test",
            "content": "description",
            "status": True,
            "published_date": datetime.now(),
        }
        response = api_client.post(url, data)
        assert response.status_code == 401

    def test_create_post_response_201_status(self, api_client, common_user):
        url = reverse("blog:api-v1:post-list")
        data = {
            "title": "test",
            "content": "description",
            "status": True,
            "published_date": '2023-12-26 12:46:26',
        }
        user = common_user
        print(datetime.now())
        api_client.force_login(user=user)
        response = api_client.post(url, data)
        assert response.status_code == 201
