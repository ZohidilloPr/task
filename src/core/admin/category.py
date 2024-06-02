from django.contrib import admin

import src.core.models as models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ("title",)
    list_display_links = ("id", "title")
    list_display = ("id", "title", "added_at")
