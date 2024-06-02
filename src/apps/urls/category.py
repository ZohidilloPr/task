from rest_framework.routers import SimpleRouter

import src.apps.views.category as views

router = SimpleRouter()
router.register("list", views.CategoryListView, basename="category-list")
router.register("detail", views.CategoryGetViewSet, basename="category-detail")
router.register("create", views.CategoryCreateView, basename="category-create")
router.register("update", views.CategoryUpdateView, basename="category-update")
router.register("delete", views.CategoryDeleteView, basename="category-delete")

urlpatterns = router.urls
