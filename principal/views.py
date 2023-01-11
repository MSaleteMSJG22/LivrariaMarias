from django.shortcuts import render
from principal.models import Produto

def index(request):
    return render(request,"index.html")

def produtos(request):
    lista = Produto.objects.all()
    context={'produtos' : lista}
    return render(request, "produtos.html",context)

def detalhes(request, id):
    produto = Produto.objects.get(id=id)
    context = {'produto':produto}
    return render(request, "detalhes.html", context)

def sobrenos(request):
    return render(request, "sobrenos.html")

def lista_produtos(request):
    lista = Produto.objects.all()
    context={'produtos' : lista}
    return render(request, 'produtos.html', context)
