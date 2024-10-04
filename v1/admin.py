from django.contrib import admin

from v1.models.breed import Breed
from v1.models.kitten import Kitten
from v1.models.rating import Rating


@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    pass


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    pass


@admin.register(Kitten)
class KittenAdmin(admin.ModelAdmin):
    pass
