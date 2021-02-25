from django.db import models


# Create your models here.

class Categoria(models.Model):
    descricao = models.CharField(max_length=32)

    def __str__(self):
        return self.descricao


class Situacao(models.Model):
    descricao = models.CharField(max_length=32)

    def __str__(self):
        return self.descricao


class Entrada(models.Model):
    data = models.DateField()
    descricao = models.CharField(max_length=32)
    quantidade_de_x_dividido = models.FloatField()
    valor_mensal = models.FloatField()
    valor_total = models.FloatField()
    categoriaentrada = models.ForeignKey(Categoria, null=True, on_delete=models.PROTECT)
    situacaoentrada = models.ForeignKey(Situacao, null=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.descricao


class Saida(models.Model):
    data = models.DateField()
    descricao = models.CharField(max_length=32)
    nome_dividendo = models.CharField(max_length=12)
    quantidade_de_x_dividido = models.FloatField()
    valor_mensal = models.FloatField()
    valor_total = models.FloatField()
    categoriasaida = models.ForeignKey(Categoria, null=True, on_delete=models.PROTECT)
    situacaosaida = models.ForeignKey(Situacao, null=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.descricao
