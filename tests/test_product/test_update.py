import pytest

from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile

from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from model_bakery import baker
import src.core.models as models


@pytest.mark.django_db
class TestUpdateProduct:
    image_path = "tests/test_media/test-img.jpg"

    @pytest.fixture
    def client(self):
        client = APIClient()
        user = User.objects.create_superuser(username='server', password='123')
        refresh = RefreshToken.for_user(user)
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        return client

    def test_update_exist_products(self, client):
        category = baker.make(models.Category)
        product = baker.make(models.Product, category=category)
        url = f'http://127.0.0.1:8000/v1/products/update/{product.pk}/'
        with open(self.image_path, 'rb') as image:
            image_file = SimpleUploadedFile(
                name='update-img.jpg',
                content=image.read(),
                content_type="image/jpeg"
            )
            data = {
                "title": "update title",
                "description": "Update description",
                "price": 15.5,
                "image": image_file,
                "category": category.pk
            }
            response = client.put(url, data, format='multipart')
            assert response.status_code == 200

            product.refresh_from_db()
            assert product.title == "update title"
            assert product.description == "Update description"
            assert product.price == 15.5
            assert product.category == category
            assert product.image.name.split('/')[-1].startswith('update-')

    def test_update_no_products(self, client):
        url = f'http://127.0.0.1:8000/v1/products/update/1000/'
        with open(self.image_path, 'rb') as image:
            image_file = SimpleUploadedFile(
                name='update-img.jpg',
                content=image.read(),
                content_type="image/jpeg"
            )
            data = {
                "title": "update title",
                "description": "Update description",
                "price": 15.5,
                "image": image_file,
                "category": 1
            }
            response = client.put(url, data, format='multipart')
            assert response.status_code == 404
