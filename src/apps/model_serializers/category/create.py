from rest_framework import serializers

import src.core.models as models


class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ("id", "title", "description", "image")
