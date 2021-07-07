from rest_framework import viewsets
from rest_framework.response import Response

from pokemon import models, serializers


class PokemonsViewSet(viewsets.ModelViewSet):
    queryset = models.Pokemon.objects.all()
    serializer_class = serializers.PokemonSerializer

    """
    CRIAR FUNÇÕES UTILIZANDO AS REQUESTS HTTP
    """