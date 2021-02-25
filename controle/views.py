from django.shortcuts import render
from .models import *

from django.shortcuts import redirect

def login(requisicao):
    return render(requisicao, 'telaDeLogin.html')

def entradas(requisicao):
    todos_entradas = Entrada.objects.all()
    if requisicao.method == 'POST':
        entrada = Entrada()
        entrada.data = requisicao.POST.get('data_entrada', None)
        entrada.quantidade_de_x_dividido = requisicao.POST.get('quantidade_de_x_dividido', None)
        entrada.valor_mensal = requisicao.POST.get('valor_mensal', None)
        entrada.valor_total = requisicao.POST.get('valor_total', None)
        if Situacao.objects.filter(descricao__iexact=requisicao.POST.get('situacaoentrada')).exists():
            entrada.situacaoentrada = Situacao.objects.get(descricao=requisicao.POST.get('situacaoentrada', None))
        if Categoria.objects.filter(descricao__iexact=requisicao.POST.get('categoriaentrada')).exists():
            entrada.categoriaentrada = Categoria.objects.get(descricao=requisicao.POST.get('categoriaentrada', None))
        entrada.save()
    contexto = {
        'entradas': todos_entradas,
        'situacaoentrada': Situacao.objects.all(),
        'categoriaentrada': Categoria.objects.all()
    }
    return render(requisicao, 'entradas.html', contexto)


def alterar_entrada(requisicao, id=None):
    if requisicao.method == 'POST':
        entrada = Entrada.objects.get(id=id)
        entrada.data = requisicao.POST.get('data_alterar', None)
        entrada.categoria.descricao = requisicao.POST.get('descricao_alterar', None)
        entrada.quantidade_de_x_dividido = requisicao.POST.get('quantidade_de_x_dividido_alterar', None)
        entrada.valor_mensal = requisicao.POST.get('valor_mensal_alterar', None)
        entrada.valor_total = requisicao.POST.get('valor_total_alterar', None)
        if Situacao.objects.filter(descricao__iexact=requisicao.POST.get('situacao_alterar')).exists():
            entrada.situacao_alterar = Situacao.objects.get(descricao=requisicao.POST.get('situacao_alterar', None))
        else:
            entrada.situacao_alterar = None
            entrada.save()
        if Categoria.objects.filter(descricao__iexact=requisicao.POST.get('categoria_alterar')).exists():
            entrada.categoria_alterar = Categoria.objects.get(descricao=requisicao.POST.get('categoria_alterar', None))
        else:
            entrada.categoria_alterar = None
            entrada.save()
    entrada.save()

    return redirect('controle:entradas')


def excluir_entrada(requisicao, id=None):
    if requisicao.method == 'POST':
        entrada = Entrada.objects.get(id=id)
        entrada.delete()
        return redirect('controle:entradas')
    return render()


def saidas(request):
    return render(request, "saidas.html")


def totalanual(request):
    return render(request, "totalanual.html")
