from rest_framework import permissions
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import RetrieveModelMixin

import src.core.models as models
import src.apps.model_serializers.category as serializers


class CategoryGetViewSet(RetrieveModelMixin, GenericViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategoryGetSerializer
    permission_classes = [permissions.IsAuthenticated]
