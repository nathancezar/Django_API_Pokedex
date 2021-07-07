from django.contrib import admin
from pokemon.models import Pokemon

class PokemonAdmin(admin.ModelAdmin):
    list_display = ('name', 'types', 'moves', 'abilities')
    list_filter = ('user', 'types', 'moves')

admin.site.register(Pokemon, PokemonAdmin)