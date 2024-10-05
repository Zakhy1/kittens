from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from v1.models.kitten import Kitten
from v1.serializers.kitten import KittenSerializer


class KittenViewSet(viewsets.ModelViewSet):
    queryset = Kitten.objects.all()
    serializer_class = KittenSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Параметр для фильтрации по породе
    breed_param = openapi.Parameter(
        'breed',
        openapi.IN_QUERY,
        description="Filter kittens by breed",
        type=openapi.TYPE_INTEGER
    )

    # Параметр для передачи JWT токена в заголовке
    jwt_auth_param = openapi.Parameter(
        'Authorization',
        openapi.IN_HEADER,
        description="JWT Authorization token",
        type=openapi.TYPE_STRING,
        required=True,
        default="Bearer <your_token>"
    )

    @swagger_auto_schema(manual_parameters=[jwt_auth_param, breed_param])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(manual_parameters=[jwt_auth_param])
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(manual_parameters=[jwt_auth_param])
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(manual_parameters=[jwt_auth_param])
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    @swagger_auto_schema(manual_parameters=[jwt_auth_param])
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    def get_queryset(self):
        breed_id = self.request.query_params.get('breed', None)
        if breed_id:
            return Kitten.objects.filter(breed_id=breed_id)
        return Kitten.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def perform_update(self, serializer):
        instance = self.get_object()
        if instance.owner != self.request.user:
            raise PermissionDenied("You cannot edit this kitten.")
        serializer.save()

    def perform_destroy(self, instance):
        if instance.owner != self.request.user:
            raise PermissionDenied("You cannot delete this kitten.")
        instance.delete()
