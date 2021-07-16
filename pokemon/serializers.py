from rest_framework import serializers
from pokemon.models import Pokemon

class PokemonSerializer(serializers.ModelSerializer):
    api_id = serializers.IntegerField(source='id')
    class Meta:
        model = Pokemon
        fields = "__all__"