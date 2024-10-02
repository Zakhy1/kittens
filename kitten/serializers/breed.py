from rest_framework import serializers

from kitten.models import Breed


class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = ['id', 'name']