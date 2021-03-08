from django.shortcuts import render
from .models import *
from .utilitarios.card import *
from django.shortcuts import redirect
from django.db.models import Sum


def login(requisicao):
    return render(requisicao, 'telaDeLogin.html')


def entradas(requisicao):
    todos_entradas = Caixa.objects.filter(tipo='entradas')
    if requisicao.method == 'POST':
        entrada = Caixa()
        entrada.data = requisicao.POST.get('data_entrada', None)
        entrada.descricao = requisicao.POST.get('descricao_entrada', None)
        entrada.quantidade_de_x_dividido = requisicao.POST.get('quantidade_de_x_dividido', None)
        entrada.valor_mensal = requisicao.POST.get('valor_mensal', None)
        entrada.valor_total = requisicao.POST.get('valor_total', None)
        entrada.tipo = 'entradas'
        entrada.situacao = requisicao.POST.get('situacao')
        if Categoria.objects.filter(descricao__iexact=requisicao.POST.get('categoriaentrada')).exists():
            entrada.categoria = Categoria.objects.get(descricao=requisicao.POST.get('categoriaentrada', None))
        else:
            categoria = Categoria(descricao=requisicao.POST.get('categoriaentrada'))
            categoria.save()
            entrada.categoria = categoria
        entrada.save()
    valor_divida_mensal = 0
    for saida in Caixa.objects.filter(tipo='saidas'):
        valor_divida_mensal = valor_divida_mensal + saida.valor_mensal
    valor_entrada_mensal = 0
    for entrada in todos_entradas:
        valor_entrada_mensal = valor_entrada_mensal + entrada.valor_mensal
    falta = valor_divida_mensal - valor_entrada_mensal
    if falta < 0:
        falta = 0
    cards = [
        Card(1, 'DIVIDA MENSAL', valor_divida_mensal, 'danger'),
        Card(1, 'ENTRADA MENSAL', valor_entrada_mensal, 'danger'),
        Card(1, 'FALTA', falta, 'danger'),
        Card(1, 'VALOR DA DIVIDA DO PROXIMO MÊS', 550, 'danger'),
    ]
    contexto = {
        'entradas': todos_entradas,
        'categoriaentrada': Categoria.objects.all(),
        'cards': cards,
    }
    return render(requisicao, 'entradas.html', contexto)


def alterar_caixa(requisicao, id=None):
    if requisicao.method == 'POST':
        caixa = Caixa.objects.get(id=id)
        caixa.data = requisicao.POST.get('data_alterar', None)
        caixa.descricao = requisicao.POST.get('descricao_alterar', None)
        caixa.quantidade_de_x_dividido = requisicao.POST.get('quantidade_de_x_dividido_alterar', None)
        caixa.valor_mensal = requisicao.POST.get('valor_mensal_alterar', None)
        caixa.valor_total = requisicao.POST.get('valor_total_alterar', None)
        caixa.situacao = requisicao.POST.get('situacao_alterar')

        if Categoria.objects.filter(descricao__iexact=requisicao.POST.get('categoria_alterar')).exists():
            caixa.categoria = Categoria.objects.get(descricao=requisicao.POST.get('categoria_alterar', None))
        else:
            categoria = Categoria(descricao=requisicao.POST.get('categoria_alterar'))
            categoria.save()
            caixa.categoria = categoria
        caixa.save()

    return redirect('controle:' + caixa.tipo)


def excluir_caixa(requisicao, id=None):
    if requisicao.method == 'POST':
        caixa = Caixa.objects.get(id=id)
        tipo = caixa.tipo
        caixa.delete()
        return redirect('controle:' + tipo)
    return render()


def saidas(requisicao, ):
    todos_saidas = Caixa.objects.filter(tipo='saidas')
    if requisicao.method == 'POST':
        saida = Caixa()
        saida.data = requisicao.POST.get('data_saida', None)
        saida.descricao = requisicao.POST.get('descricao_saida', None)
        saida.quantidade_de_x_dividido = requisicao.POST.get('quantidade_de_x_dividido', None)
        saida.valor_mensal = requisicao.POST.get('valor_mensal', None)
        saida.valor_total = requisicao.POST.get('valor_total', None)
        saida.tipo = 'saidas'
        saida.situacao = requisicao.POST.get('situacao')
        if Categoria.objects.filter(descricao__iexact=requisicao.POST.get('categoriasaida')).exists():
            saida.categoria = Categoria.objects.get(descricao=requisicao.POST.get('categoriasaida', None))
        else:
            categoria = Categoria(descricao=requisicao.POST.get('categoriasaida'))
            categoria.save()
            saida.categoria = categoria
        saida.save()

    contexto = {
        'saidas': todos_saidas,
        'categoriasaida': Categoria.objects.all(),

    }
    return render(requisicao, "saidas.html", contexto)


def totalanual(request):
    totalentradas = []
    for x in range(1, 13):
        valores = Caixa.objects.filter(tipo='entradas', data__month=x).aggregate(Sum('valor_mensal')).get('valor_mensal__sum')
        if valores is not None:
            totalentradas.append(valores)
        else:
            totalentradas.append(0)
    contexto = {
        'totalentradas': totalentradas
    }
    return render(request, "totalanual.html", contexto)
