from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied

from rest_framework.permissions import IsAuthenticatedOrReadOnly

from v1.models.rating import Rating
from v1.schema import jwt_auth
from v1.serializers.rating import RatingSerializer


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    # TODO юзера нельзя изменить, только для чтения
    @swagger_auto_schema(manual_parameters=[jwt_auth])
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(manual_parameters=[jwt_auth])
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(manual_parameters=[jwt_auth])
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(manual_parameters=[jwt_auth])
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    def perform_update(self, serializer):
        # Запрещаем изменять данные об оценке, если пользователь не является ее создателем
        instance = self.get_object()
        if instance.user != self.request.user:
            raise PermissionDenied("You cannot edit this rate.")
        serializer.save()

    def perform_destroy(self, instance):
        # Запрещаем удалять оценку, если пользователь не является ее создателем
        if instance.user != self.request.user:
            raise PermissionDenied("You cannot delete this rate.")
        instance.delete()
