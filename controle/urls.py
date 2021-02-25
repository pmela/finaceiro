from django.urls import path
from .views import *

app_name='controle'

urlpatterns = [
    path('entradas', entradas, name='entradas'),
    path('saidas', saidas, name='saidas'),
    path('totalanual', totalanual, name='totalanual'),
]
