from django.shortcuts import render, redirect
# importamos la libreria generic
from django.views import View
from .models import *
from .forms import *

# Create your views here.

class PrincipalView(View):
    def get(self, request):
        listaAlumnos = TblAlumnos.objects.all()
        listaProfesores = TblProfesores.objects.all()
        formAlumno = AlumnoForm()
        formProfesor = ProfesorForm()

        context = {
            'alumnos': listaAlumnos,
            'profesores': listaProfesores,
            'formAlumno': formAlumno,
            'formProfesor': formProfesor
        }
        return render(request, 'index.html', context)

    def post(self, request):
        form_type = request.POST.get('form_type')

        if form_type == "alumno":
            formAlumno = AlumnoForm(request.POST)
            if formAlumno.is_valid():
                formAlumno.save()
                return redirect('web:index_principal')
        
        elif form_type == "profesor":
            formProfesor = ProfesorForm(request.POST)
            if formProfesor.is_valid():
                formProfesor.save()
                return redirect('web:index_principal')

        # Si algo falla o no se envía un formulario válido, simplemente volvemos a cargar la página.
        return self.get(request)

class EliminarView(View):
    def get(self, request, id):
        alumno = TblAlumnos.objects.filter(alumno_id=id).first()
        profesor = TblProfesores.objects.filter(profesor_id=id).first()
        if alumno:
            alumno.delete()
        elif profesor:
            profesor.delete()
        return redirect('/')  # Redirige a la vista con el nombre 'index'




# class EliminarView(View):
#     def get(self, request, id):
#         tarea = get_object_or_404(TblAlumnos, alumno_id=id)
#         tarea = get_object_or_404(TblProfesores, profesor_id=id)
#         tarea.delete()
#         return redirect(request,'index.html')