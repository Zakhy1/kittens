from django.contrib.auth import get_user_model
from django.db import models


class Rating(models.Model):
    kitten = models.ForeignKey('Kitten', on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    score = models.PositiveIntegerField(choices=[(i, str(i)) for i in range(1, 6)])