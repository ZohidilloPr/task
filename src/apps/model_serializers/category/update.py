from rest_framework import serializers

import src.core.models as models


class CategoryUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ("id", "title", "description", "image", "added_at")

