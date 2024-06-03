from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from elasticsearch_dsl.query import MultiMatch
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import LimitOffsetPagination

import src.shared as shared
import src.apps.model_serializers as serializers


class ProductSearchListView(APIView, LimitOffsetPagination):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        query = request.query_params.get('query')
        if query:
            q = MultiMatch(
                query=query,
                fields=[
                    "title",
                    "description"
                ], fuzziness='AUTO'
            )
            search_doc = shared.ProductDocument.search().query(q)
            response = search_doc.execute()
            results = self.paginate_queryset(response, request, view=self)
            serializer = serializers.ProductDocumentSerializer(results, many=True)
            return self.get_paginated_response(serializer.data)

        return Response({"Products": []}, status=status.HTTP_404_NOT_FOUND)
