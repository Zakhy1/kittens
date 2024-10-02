from rest_framework import viewsets

from kitten.models import Breed
from kitten.serializers.breed import BreedSerializer


class BreedViewSet(viewsets.ModelViewSet):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
    http_method_names = ['get']
