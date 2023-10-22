from django.shortcuts import render
from .models import *

def home(request):
    recetas = Receta.objects.all()
    context = {'recetas': recetas}
    return render(request, 'recetas/home.html', context)

