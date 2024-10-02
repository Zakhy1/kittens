from django.contrib.auth import get_user_model
from django.db import models


class Breed(models.Model):
    name = models.CharField(max_length=100)


class Kitten(models.Model):
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    color = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    description = models.TextField()
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)


class Rating(models.Model):
    kitten = models.ForeignKey(Kitten, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    score = models.PositiveIntegerField(choices=[(i, str(i)) for i in range(1, 6)])
