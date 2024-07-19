
from django.contrib import admin
from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

name_api = 'Expenses Website'
schema_view = get_schema_view(
    openapi.Info(
        title=f"Documentación de la API {name_api}",
        default_version='v1',
        description=f"Documentación de la API {name_api}",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="djangoproject@correo.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    #path('redocs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
