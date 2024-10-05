from rest_framework import viewsets

from v1.models.breed import Breed
from v1.serializers.breed import BreedSerializer


class BreedViewSet(viewsets.ModelViewSet):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
    http_method_names = ['get']
