from rest_framework import serializers

import src.core.models as models


class CategoryGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ("id", "title", "description", "image", "added_at")

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["added_at"] = instance.added_at.strftime("%Y-%m-%d %H:%M")
        return data
