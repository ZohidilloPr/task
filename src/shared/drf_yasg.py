# from rest_framework_swagger.views import get_swagger_view
from drf_yasg import openapi
from django.contrib import admin
from rest_framework import permissions
from drf_yasg.views import get_schema_view

API_TITLE = 'Tafakkur Group Tasks'
API_DESCRIPTION = 'Tafakkur Group Task docs'

yasg_schema_view = get_schema_view(
    openapi.Info(
        title=API_TITLE,
        default_version='v1',
        description=API_DESCRIPTION,
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="turgunovzohidillo77@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# schema_view = get_swagger_view(title=API_TITLE)


admin.site.site_header = "Tafakkur Group"
admin.site.site_title = "Tafakkur Group"
admin.site.index_title = "Tafakkur Group"
