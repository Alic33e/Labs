from django.db import models

class TblAlumnos(models.Model):
    alumno_id = models.AutoField(primary_key=True)
    alumno_nombre = models.CharField(max_length=100)
    alumno_email = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.alumno_nombre

class TblProfesores(models.Model):
    profesor_id = models.AutoField(primary_key=True)
    profesor_nombre = models.CharField(max_length=255)
    profesor_email = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.profesor_nombre
