from rest_framework import permissions
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin

import src.core.models as models
import src.apps.model_serializers as serializers


class CategoryCreateView(CreateModelMixin, GenericViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategoryCreateSerializer
    permission_classes = [permissions.IsAuthenticated]
