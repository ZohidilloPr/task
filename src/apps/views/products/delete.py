from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import DestroyModelMixin
from rest_framework.permissions import IsAuthenticated

import src.core.models as models


class ProductDeleteView(DestroyModelMixin, GenericViewSet):
    queryset = models.Product.objects.select_related('category')
    permission_classes = [IsAuthenticated]
