from rest_framework.routers import DefaultRouter
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from v1.schema import schema_view
from v1.views.breed import BreedViewSet
from v1.views.kitten import KittenViewSet
from v1.views.rating import RatingViewSet

router = DefaultRouter()

router.register('breeds', BreedViewSet, basename='breed')
router.register('kittens', KittenViewSet, basename='kitten')
router.register('ratings', RatingViewSet, basename='rating')

urlpatterns = [
    # API
    path('', include(router.urls)),
    # JWT
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # swagger
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('swagger.yaml/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
]
