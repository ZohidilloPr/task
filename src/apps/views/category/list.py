from rest_framework import permissions
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet

import src.shared as shared
import src.core.models as models
import src.apps.model_serializers as serializers


class CategoryListView(ListModelMixin, GenericViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategoryListSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = shared.CustomPagination
