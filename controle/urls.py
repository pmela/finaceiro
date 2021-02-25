from django.urls import path
from .views import *

urlpatterns = [
    path('entradas', entradas, name='entradas'),
    path('saidas', saidas, name='saidas'),
]
