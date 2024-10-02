from django.contrib import admin

from kitten.models.breed import Breed
from kitten.models.kitten import Kitten
from kitten.models.rating import Rating


@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    pass


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    pass


@admin.register(Kitten)
class KittenAdmin(admin.ModelAdmin):
    pass
