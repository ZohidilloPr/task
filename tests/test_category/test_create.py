import locale
import pytest

from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile

from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

encoding = locale.getencoding() or 'ascii'


@pytest.mark.django_db
class TestCreateCategory:
    @pytest.fixture
    def client(self):
        client = APIClient()
        user = User.objects.create_superuser(username='server', password='123')
        refresh = RefreshToken.for_user(user)
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        return client

    def test_create_category(self, client):
        url = 'http://127.0.0.1:8000/v1/category/create/'
        image_path = "tests/test_media/test-img.jpg"
        with open(image_path, 'rb') as image:
            image_file = SimpleUploadedFile(
                name='test-img.jpg',
                content=image.read(),
                content_type="image/jpeg"
            )
            data = {
                "title": "title",
                "description": "description",
                "image": image_file,
            }
            response = client.post(url, data, format='multipart')
            assert response.status_code == 201
