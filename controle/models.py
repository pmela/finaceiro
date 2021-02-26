from django.db import models


class Categoria(models.Model):
    descricao = models.CharField(max_length=32)

    def __str__(self):
        return self.descricao


class Caixa(models.Model):
    data = models.DateField()
    descricao = models.CharField(max_length=32)
    quantidade_de_x_dividido = models.FloatField()
    nome_devedor = models.CharField(max_length=12, null=True, blank=True)
    valor_mensal = models.FloatField()
    valor_total = models.FloatField()
    tipo = models.CharField(max_length=8, choices=[("entradas", "Entradas"), ("saidas", "Saídas")])
    situacao = models.CharField(max_length=8, choices=[("fixo", "Fixo"), ("variavel", "Variável")])
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)

    def __str__(self):
        return self.descricao
