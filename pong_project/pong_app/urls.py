from django.urls import path
from .views import create_player, index

urlpatterns = [
    path('players/', create_player, name='create_player'),
    path('', index, name='index'),
]
