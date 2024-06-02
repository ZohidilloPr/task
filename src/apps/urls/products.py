from django.urls import path
from rest_framework.routers import SimpleRouter

import src.apps.views.products as views

router = SimpleRouter()
router.register("list", views.ProductListView, basename="product-list")
router.register("detail", views.ProductGetView, basename="product-detail")
router.register("create", views.ProductCreateView, basename="product-create")
router.register("update", views.ProductUpdateView, basename="product-update")
router.register("delete", views.ProductDeleteView, basename="product-delete")

urlpatterns = [
                  path("e_search/", views.ProductSearchListView.as_view())
              ] + router.urls
