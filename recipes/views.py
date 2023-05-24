from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'recipes/home.html', context={'name':'Site backsate LILIANE AMANDA DA SILVA',})

def contato(request):
    return HttpResponse('contato')

def sobre(request):
    return HttpResponse('sobre')


# Create your views here.
