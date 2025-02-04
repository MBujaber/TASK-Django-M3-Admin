from email.policy import default
from operator import mod
from random import choices
from django.db import models


# Create your models here.
class Pokemon(models.Model):
    class PokemonType(models.TextChoices):
        WATER = 'WA'
        GRASS = 'GR'
        GHOST = 'GH'
        STEEL = 'ST'
        FAIRY = 'FA'

    name = models.CharField(max_length=30)
    type = models.CharField(max_length=60, choices=PokemonType.choices)
    hp = models.PositiveIntegerField()
    active = models.BooleanField(default=True)
    name_fr = models.CharField(max_length=30, default="", blank=True)
    name_ar = models.CharField(max_length=30, default="")
    name_jp = models.CharField(max_length=30, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # description = models.TextField(default="")
    # opening_time = models.TimeField()
    # closing_time = models.TimeField()
    # created_at = models.TimeField(auto_now_add=True)
