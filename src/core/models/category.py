from django.db import models

import src.core.models as model


class Category(model.BaseModel):
    image = models.ImageField(upload_to='category/', verbose_name='Category Image')

    class Meta:
        db_table = 'categories'
        ordering = ("-added_at",)
        verbose_name = 'Categories'
        verbose_name_plural = 'Categories'

