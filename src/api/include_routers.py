from django.urls import path, include

urlpatterns = [
    path('', include("src.apps.urls.account")),
    path("category/", include("src.apps.urls.category")),
    path("products/", include("src.apps.urls.products")),
]