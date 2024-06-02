from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import IsAuthenticated

import src.core.models as models
import src.apps.model_serializers as serializers


class ProductCreateView(CreateModelMixin, GenericViewSet):
    queryset = models.Product.objects.select_related('category')
    serializer_class = serializers.ProductCreateSerializer
    permission_classes = [IsAuthenticated]
