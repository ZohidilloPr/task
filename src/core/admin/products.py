from django.contrib import admin

import src.core.models as models


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ('id', 'title', 'price', 'added_at')
    list_display_links = ('id', 'title')
