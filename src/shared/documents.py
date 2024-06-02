from django_elasticsearch_dsl import Document, Index
from django_elasticsearch_dsl.registries import registry

import src.core.models as models

product_index = Index("products_index")


@product_index.doc_type
class ProductDocument(Document):
    class Django:
        model = models.Product
        fields = ("title", "description", "price")
