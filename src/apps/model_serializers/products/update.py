from rest_framework import serializers

import src.core.models as models


class ProductUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = ("id", "title", "description", "category", "price", "image", "added_at")

