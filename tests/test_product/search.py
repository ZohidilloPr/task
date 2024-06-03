import locale
import pytest

from django.contrib.auth.models import User

from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from model_bakery import baker
import src.core.models as models

encoding = locale.getencoding() or 'ascii'


@pytest.mark.django_db
class TestSearchListProduct:
    @pytest.fixture
    def client(self):
        client = APIClient()
        user = User.objects.create_superuser(username='server', password='123')
        refresh = RefreshToken.for_user(user)
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        return client

    def test_search_list_products(self, client):
        baker.make(models.Product, __quantity__=10)
        url = 'http://127.0.0.1:8000/v1/products/list/'
        response = client.get(url)
        assert response.status_code == 200
