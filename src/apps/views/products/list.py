from elasticsearch_dsl import Q
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

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


class ProductSearchListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        query = request.query_params.get('query', None)
        if query:
            q = Q("multi_match", query=query, fields=["title", "description", "price"])
            search_doc = shared.ProductDocument.search().query(q)
            response = search_doc.execute()
            serializer = serializers.ProductDocumentSerializer(response, many=True)
            return Response(serializer.data)
        return Response({"Products": []}, status=status.HTTP_404_NOT_FOUND)
