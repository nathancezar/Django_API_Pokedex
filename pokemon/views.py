from rest_framework import viewsets, status
from rest_framework.response import Response

from pokemon import models, serializers
from pokemon.integrations.pokeapi import PokeApi


class PokemonsViewSet(viewsets.ModelViewSet):

    queryset = models.Pokemon.objects.all()
    serializer_class = serializers.PokemonSerializer
    lookup_field = "name"

    def get_pokemon(self, name=None):
        if name:
            pokemon_response = PokeApi().get_pokemon_by_name(name)
            print(pokemon_response)

        elif id:
            pokemon_response = PokeApi().get_pokemon_by_id(id)
            print(pokemon_response)

    def remove_pokemon(self, name=None):
        pass

    def retrieve(self, request, name=None):
        """
        Busca um pokemon na PokeApi e salva no banco de dados

        :id: numero do pokemon
        :name: nome do pokemon
        """
        # import ipdb; ipdb.set_trace(context=10)
        if request.method == 'GET':
            try:
                new_pokemon = self.get_pokemon(id, name)
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)

            return Response(self.serializer_class(new_pokemon).data, \
                status=status.HTTP_200_OK)

        if request.method == 'DELETE':
            try:
                self.remove_pokemon(id, name)
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)