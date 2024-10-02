from rest_framework import serializers

from kitten.models import Kitten


class KittenSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Kitten
        fields = ['id', 'breed', 'color', 'age', 'description', 'owner']