import locale
import pytest

from django.contrib.auth.models import User

from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from model_bakery import baker
import src.core.models as models

encoding = locale.getencoding() or 'ascii'


@pytest.mark.django_db
class TestDeleteProduct:
    @pytest.fixture
    def client(self):
        client = APIClient()
        user = User.objects.create_superuser(username='server', password='123')
        refresh = RefreshToken.for_user(user)
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        return client

    def test_delete_exist_products(self, client):
        category = baker.make(models.Category)
        product = baker.make(models.Product, category=category)
        url = f'http://127.0.0.1:8000/v1/products/delete/{product.pk}/'
        response = client.delete(url)
        assert response.status_code == 204

    def test_delete_no_product(self, client):
        url = f'http://127.0.0.1:8000/v1/products/delete/1000/'
        response = client.delete(url)
        assert response.status_code == 404


