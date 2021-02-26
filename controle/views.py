from django.shortcuts import render
from .models import *
from .utilitarios.card import *
from django.shortcuts import redirect


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


def alterar_entrada(requisicao, id=None):
    if requisicao.method == 'POST':
        entrada = Caixa.objects.get(id=id)
        entrada.data = requisicao.POST.get('data_alterar', None)
        entrada.categoria.descricao = requisicao.POST.get('descricao_alterar', None)
        entrada.quantidade_de_x_dividido = requisicao.POST.get('quantidade_de_x_dividido_alterar', None)
        entrada.valor_mensal = requisicao.POST.get('valor_mensal_alterar', None)
        entrada.valor_total = requisicao.POST.get('valor_total_alterar', None)
        entrada.tipo = requisicao.POST.get('tipo', None)
        if Categoria.objects.filter(descricao__iexact=requisicao.POST.get('categoria_alterar')).exists():
            entrada.categoria = Categoria.objects.get(descricao=requisicao.POST.get('categoria_alterar', None))
        else:
            categoria = Categoria(descricao=requisicao.POST.get('categoria_alterar'))
            categoria.save()
            entrada.categoria = categoria
        entrada.save()

    return redirect('controle:entradas')


def excluir_entrada(requisicao, id=None):
    if requisicao.method == 'POST':
        entrada = Caixa.objects.get(id=id)
        entrada.delete()
        return redirect('controle:entradas')
    return render()


def saidas(request):
    return render(request, "saidas.html")


def totalanual(request):
    return render(request, "totalanual.html")
