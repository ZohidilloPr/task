import locale
import pytest

from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile

from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from model_bakery import baker
import src.core.models as models

encoding = locale.getencoding() or 'ascii'


@pytest.mark.django_db
class TestUpdateCategory:
    image_path = "tests/test_media/test-img.jpg"

    @pytest.fixture
    def client(self):
        client = APIClient()
        user = User.objects.create_superuser(username='server', password='123')
        refresh = RefreshToken.for_user(user)
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        return client

    def test_create_category(self, client):
        category = baker.make(models.Category)
        url = f'http://127.0.0.1:8000/v1/category/update/{category.pk}/'
        with open(self.image_path, 'rb') as image:
            image_file = SimpleUploadedFile(
                name='update-img.jpg',
                content=image.read(),
                content_type="image/jpeg"
            )
            data = {
                "title": "update title",
                "description": "update description",
                "image": image_file,
            }
            response = client.put(url, data, format='multipart')
            assert response.status_code == 200
            category.refresh_from_db()
            assert category.title == "update title"
            assert category.description == "update description"
            assert category.image.name.split("/")[-1].startswith("update-")

    def test_create_no_category(self, client):
        url = f'http://127.0.0.1:8000/v1/category/update/1000/'
        with open(self.image_path, 'rb') as image:
            image_file = SimpleUploadedFile(
                name='update-img.jpg',
                content=image.read(),
                content_type="image/jpeg"
            )
            data = {
                "title": "update title",
                "description": "update description",
                "image": image_file,
            }
            response = client.put(url, data, format='multipart')
            assert response.status_code == 404
