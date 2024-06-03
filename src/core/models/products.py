from django.db import models

import src.core.models as model


class Product(model.BaseModel):
    category = models.ForeignKey(model.Category, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='products/', verbose_name='Product Image')
    price = models.DecimalField(max_digits=15, decimal_places=2)

    class Meta:
        db_table = 'products'
        ordering = ("-added_at",)
        verbose_name = 'Products'
        verbose_name_plural = 'Products'
