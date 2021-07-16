from django.urls import include, path
from rest_framework.routers import DefaultRouter

from pokemon import views


router = DefaultRouter()
router.register(r'pokemon', views.PokemonsViewSet)

urlpatterns = [path("", include(router.urls))]
