from rest_framework import viewsets

from rest_framework.permissions import IsAuthenticated

from kitten.models import Rating
from kitten.serializers.rating import RatingSerializer


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
