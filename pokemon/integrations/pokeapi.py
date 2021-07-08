import os
import requests


class PokeApi:
    API_URL = os.environ.get("POKEAPI_URL", "https://pokeapi.co/api/v2/")

    def get_pokemon_by_name(self, name: str):
        """Busca um pokemon na pokeapi

        :name: nome do pokemon
        """
        pokeapi_responde = requests.get(
            f"{self.API_URL}/{name}"
        )
        pokeapi_responde.raise_for_status()

        return pokeapi_responde

    def get_pokemon_by_id(self, id: int):
        """Busca um pokemon na pokeapi

        :id: numero do pokemon
        """
        pokeapi_responde = requests.get(
            f"{self.API_URL}/{id}"
        )
        pokeapi_responde.raise_for_status()

        return pokeapi_responde