from django.urls import path

from . import views

app_name='operaciones'

urlpatterns = [
    path('calculadora',views.calculadora,name='calculadora'),
    path('resultadoope',views.resultado,name='resultadoope'),
    path('datos-cilindro',views.datosCilindro,name='datosCilindro'),
    path('resultVolumen',views.resultVolumen,name='resultVolumen')
]