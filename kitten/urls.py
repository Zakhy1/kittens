from rest_framework.routers import DefaultRouter
from django.urls import path, include

from kitten.views.breed import BreedViewSet
from kitten.views.kitten import KittenViewSet
from kitten.views.rating import RatingViewSet

router = DefaultRouter()

router.register('breeds', BreedViewSet, basename='breed')
router.register('kittens', KittenViewSet, basename='kitten')
router.register('ratings', RatingViewSet, basename='rating')

urlpatterns = [
    path('', include(router.urls)),
]
