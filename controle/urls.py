from django.urls import path
from .views import *

app_name = 'controle'

urlpatterns = [
    path('entradas', entradas, name='entradas'),
    path('saidas', saidas, name='saidas'),
    path('alterarcaixa/<int:id>', alterar_caixa, name='alterarcaixa'),
    path('excluir_caixa/<int:id>', excluir_caixa, name='excluir_caixa'),
    path('totalanual', totalanual, name='totalanual'),
    path('login', login, name='login')
]
