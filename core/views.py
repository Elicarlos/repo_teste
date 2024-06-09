from django.http import HttpResponse
from django.shortcuts import render
from . models import Tipo

# Create your views here.
def home(request):
    return render(request, 'core/index.html')


def produto(request):
    return render(request, 'core/produto.html')


def list_produto(request):
    tipos = Tipo.objects.all()
    
    for tipo in tipos:
        print(tipo)
    context = {
        'tipos': tipos
    }
    
    return render(request, 'core/list-produto.html', context)
