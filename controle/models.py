from django.db import models


# Create your models here.


class Entradas(models.Model):
    data = models.DateField()
    descricao = models.CharField(max_length=32)
    situacao = models.CharField(max_length=12)
    quantidade_de_x_dividido = models.FloatField()
    valor_mensal = models.FloatField()
    valor_total = models.FloatField()

    def __str__(self):
     return self.descricao


class Saidas(models.Model):
    data = models.DateField()
    descricao = models.CharField(max_length=32)
    situacao = models.CharField(max_length=12)
    nome_dividendo = models.CharField(max_length=12)
    quantidade_de_x_dividido = models.FloatField()
    valor_mensal = models.FloatField()
    valor_total = models.FloatField()

    def __str__(self):
     return self.descricao
