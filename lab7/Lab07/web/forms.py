from django.forms import ModelForm
from .models import *

class AlumnoForm(ModelForm):
    class Meta:
        model = TblAlumnos
        fields = '__all__'

class ProfesorForm(ModelForm):
    class Meta:
        model = TblProfesores
        fields = '__all__'
