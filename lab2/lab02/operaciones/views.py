from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def calculadora(request):
    context = {
        'titulo' : "Ingrese los numeros",
    }
    return render(request,'operaciones/formulario.html',context)

def resultado(request):
    a=request.POST['numeroa']
    b=request.POST['numerob']
    if request.POST['operacion'] == 'suma':
        resultado= int(a)+int(b)
    if request.POST['operacion'] == 'resta':
        resultado= int(a)-int(b)
    if request.POST['operacion'] == 'multiplicacion':
        resultado= int(a)*int(b)

    context = {
        'operacion' : request.POST['operacion'],
        'numeroa' : request.POST['numeroa'],
        'numerob' : request.POST['numerob'],
        'titulo' : "Resultado de la operación",
        'resultado' :resultado  
    }
    return render(request,'operaciones/resultados.html',context)

def datosCilindro(request):
    context = {
        'titulo' : "CÁLCULO DEL VOLUMEN DE UN CILINDRO "
    }
    return render(request,'operaciones/formCilindro.html',context)

def resultVolumen(request):
    diametro=request.POST['diametro']
    altura=request.POST['altura']
    radio=float(diametro)/2
    volumen=(3.1416*(radio)**2)*float(altura)

    context = {
        'titulo' : 'VOLUMEN DEL CILINDRO',
        'volumen' : volumen
    }

    return render(request,'operaciones/resultVolumen.html',context)
