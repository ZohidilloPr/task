from rest_framework import permissions
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import UpdateModelMixin

import src.core.models as models
import src.apps.model_serializers as serializers


class CategoryUpdateView(UpdateModelMixin, GenericViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategoryUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]
