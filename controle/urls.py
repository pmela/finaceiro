from django.urls import path
from .views import *

app_name='controle'

urlpatterns = [
    path('entradas', entradas, name='entradas'),
    path('alterarentrada/<int:id>', alterar_entrada, name='alterarentrada'),
    path('excluir_entrada/<int:id>', excluir_entrada, name='excluir_entrada'),
    path('saidas', saidas, name='saidas'),
    path('totalanual', totalanual, name='totalanual'),
]
