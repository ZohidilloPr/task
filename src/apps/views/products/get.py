from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated

import src.core.models as models
import src.apps.model_serializers as serializers


class ProductGetView(RetrieveModelMixin, GenericViewSet):
    queryset = models.Product.objects.select_related('category')
    serializer_class = serializers.ProductGetSerializer
    permission_classes = [IsAuthenticated]
