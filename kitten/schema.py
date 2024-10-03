from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Kitten API",
        default_version='v1',
        description="API for managing kittens and their breeds",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
