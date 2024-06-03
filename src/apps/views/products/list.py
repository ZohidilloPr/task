from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated

import src.shared as shared
import src.core.models as models
import src.apps.model_serializers as serializers


class ProductListView(ListModelMixin, GenericViewSet):
    queryset = models.Product.objects.select_related('category')
    serializer_class = serializers.ProductListSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = shared.CustomPagination
