from django.shortcuts import render
from .models import *


def entradas(request):
    return render(request, "entradas.html")


def saidas(request):
    return render(request, "saidas.html")


def totalanual(request):
    return render(request, "totalanual.html")
