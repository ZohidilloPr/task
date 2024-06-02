from rest_framework import serializers

import src.shared as shared


class ProductDocumentSerializer(serializers.Serializer):
    class Meta:
        model = shared.ProductDocument
        fields = ("title", "description", "price")


