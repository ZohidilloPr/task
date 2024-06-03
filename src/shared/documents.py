from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry

import src.core.models as models


@registry.register_document
class ProductDocument(Document):
    id = fields.IntegerField(attr="id")

    category = fields.ObjectField(
        properties={
            "id": fields.IntegerField(),
            "title": fields.TextField(),
            "description": fields.TextField()
        }
    )

    class Index:
        name = 'products'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }

    class Django:
        model = models.Product
        fields = (
            "title",
            "description",
            "price",
            "image",
            "added_at"
        )

    def get_queryset(self):
        return super(ProductDocument, self).get_queryset().select_related(
            'category'
        )
