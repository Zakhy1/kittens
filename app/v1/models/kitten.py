from django.contrib.auth.models import User
from django.db import models


class Kitten(models.Model):
    breed = models.ForeignKey('Breed', on_delete=models.CASCADE)
    color = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)