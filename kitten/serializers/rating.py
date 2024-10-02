from rest_framework import serializers

from kitten.models.rating import Rating


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'kitten', 'user', 'score']