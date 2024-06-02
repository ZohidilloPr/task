from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import UpdateModelMixin
from rest_framework.permissions import IsAuthenticated

import src.core.models as models
import src.apps.model_serializers as serializers


class ProductUpdateView(UpdateModelMixin, GenericViewSet):
    queryset = models.Product.objects.select_related('category')
    serializer_class = serializers.ProductUpdateSerializer
    permission_classes = [IsAuthenticated]
