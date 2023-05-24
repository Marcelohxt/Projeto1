from django.shortcuts import render

def home(request):
    return render(request, 'recipes/home.html', context={'name':'Site backsate LILIANE AMANDA DA SILVA',})




# Create your views here.
