from rest_framework import serializers

import src.core.models as models
import src.apps.model_serializers as serializer


class ProductGetSerializer(serializers.ModelSerializer):
    category = serializer.CategoryGetSerializer()

    class Meta:
        model = models.Product
        fields = ("id", "title", "description", "category", "price", "image", "added_at")

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["added_at"] = instance.added_at.strftime("%Y-%m-%d %H:%M")
        return data

