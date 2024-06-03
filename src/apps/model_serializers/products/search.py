from rest_framework import serializers

import src.core.models as models


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ("id", "title", "description")


class ProductDocumentSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    description = serializers.CharField()
    price = serializers.FloatField()
    image = serializers.CharField()
    category = CategorySerializer(read_only=True)
    added_at = serializers.DateTimeField()
