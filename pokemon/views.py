from typing import Union
from rest_framework import viewsets
from rest_framework.response import Response

from pokemon import models, serializers
from pokemon.integrations.pokeapi import PokeApi


class PokemonsViewSet(viewsets.ModelViewSet):

    queryset = models.Pokemon.objects.all()
    serializer_class = serializers.PokemonSerializer

    def add_pokemon(self, id=None, name=None):
        pass