from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, permissions
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from v1.models.kitten import Kitten
from v1.schema import jwt_auth
from v1.serializers.kitten import KittenSerializer


class KittenViewSet(viewsets.ModelViewSet):
    queryset = Kitten.objects.all()
    serializer_class = KittenSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    @swagger_auto_schema(manual_parameters=[jwt_auth])
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(manual_parameters=[jwt_auth])
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(manual_parameters=[jwt_auth])
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    @swagger_auto_schema(manual_parameters=[jwt_auth])
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        breed_id = self.request.query_params.get('breed', None)
        if breed_id:
            return Kitten.objects.filter(breed_id=breed_id)
        return Kitten.objects.all()

    def perform_update(self, serializer):
        # Запрещаем изменять данные о котенке, если пользователь не является владельцем
        instance = self.get_object()
        if instance.owner != self.request.user:
            raise PermissionDenied("You cannot edit this kitten.")
        serializer.save()

    def perform_destroy(self, instance):
        # Запрещаем удалять котенка, если пользователь не является владельцем
        if instance.owner != self.request.user:
            raise PermissionDenied("You cannot delete this kitten.")
        instance.delete()
