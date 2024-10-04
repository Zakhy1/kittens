from rest_framework import serializers
from v1.models.rating import Rating


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'kitten', 'user', 'score']

    def update(self, instance, validated_data):
        # Удаляем поле user из обновляемых данных
        validated_data.pop('user', None)
        return super().update(instance, validated_data)

    def validate(self, attrs):
        # Если пользователь пытается изменить поле user, выбрасываем ошибку
        if 'user' in attrs and attrs['user'] != self.instance.user:
            raise serializers.ValidationError({"user": "Cannot change user."})
        return attrs
