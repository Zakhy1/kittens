from rest_framework.routers import DefaultRouter
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from kitten.schema import schema_view
from kitten.views.breed import BreedViewSet
from kitten.views.kitten import KittenViewSet
from kitten.views.rating import RatingViewSet

router = DefaultRouter()

router.register('breeds', BreedViewSet, basename='breed')
router.register('kittens', KittenViewSet, basename='kitten')
router.register('ratings', RatingViewSet, basename='rating')

urlpatterns = [
    # API
    path('', include(router.urls)),
    # JWT
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # swagger
    path('api/v1/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
