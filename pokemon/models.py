from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey

class Types(models.Model):
    api_id = models.PositiveSmallIntegerField(null=True)
    name = models.CharField(max_length=50, null=False)
    # damage_relations = models.ForeignKey(TypeRelations, null=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = 'types'

    def __str__(self) -> str:
        return self.name

class Abilities(models.Model):
    api_id = models.PositiveSmallIntegerField(null=False)
    name = models.CharField(max_length=50, null=False)

    class Meta:
        db_table = 'abilities'

    def __str__(self) -> str:
        return self.name

class Species(models.Model):
    api_id = models.PositiveSmallIntegerField()
    name = models.CharField(max_length=50, null=False)
    order = models.IntegerField()
    is_legendary = models.BooleanField()
    is_mythical = models.BooleanField()

    class Meta:
        db_table = 'species'

    def __str__(self) -> str:
        return self.name

class Moves(models.Model):
    api_id = models.PositiveSmallIntegerField(null=False)
    name = models.CharField(max_length=50, null=False)
    accuracy = models.SmallIntegerField()
    effect_chance = models.SmallIntegerField()
    power_points = models.SmallIntegerField()
    power = models.SmallIntegerField()

    class Meta:
        db_table = 'moves'

    def __str__(self) -> str:
        return self.name

class Forms(models.Model):
    api_id = models.PositiveSmallIntegerField(null=False)
    name = models.CharField(max_length=50, null=False)
    is_default = models.BooleanField()
    is_mega = models.BooleanField()
    form_name = models.CharField(max_length=50)

    class Meta:
        db_table = 'forms'

    def __str__(self) -> str:
        return self.name

class Pokemon(models.Model):
    api_id = models.PositiveSmallIntegerField(null=False)
    name = models.CharField(max_length=50, null=False)
    base_experience = models.IntegerField()
    height = models.IntegerField()
    is_default = models.BooleanField()
    weight = models.IntegerField()
    abilities = models.ForeignKey(Abilities, null=True, on_delete=models.SET_NULL)
    forms = models.ForeignKey(Forms, null=True, on_delete=models.SET_NULL)
    location_area_encounters = models.CharField(max_length=100)
    moves = models.ForeignKey(Moves, null=True, on_delete=models.SET_NULL)
    species = models.ForeignKey(Species, null=True, on_delete=models.SET_NULL)
    types = models.ForeignKey(Types, null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'pokemon'

    def __str__(self) -> str:
        return self.name
