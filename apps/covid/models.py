from django.db import models
from apps.users.models import User
class Doctor(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
class Laboratorista(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
class Minsal(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
class Departamento(models.Model):
    idDepartamento = models.AutoField(primary_key=True)
    nombre_departamento = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_departamento

class Municipio(models.Model):
    idMunicipio = models.AutoField(primary_key=True)
    departamento = models.ForeignKey(Departamento, null = True, blank = True, on_delete=models.CASCADE)
    nombre_municipio = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre_municipio

class Paciente(models.Model):
    idPaciente = models.AutoField(primary_key=True)
    nombre_paciente = models.CharField(max_length=50, null = False, blank = False)
    apellido_paciente = models.CharField(max_length=50, null = False, blank = False)
    dui_paciente = models.CharField(max_length=9, null=False, blank = False)
    sexo_paciente = models.BooleanField()
    fecha_paciente = models.DateTimeField()
class CuadroMedico(models.Model):
    idCuadroMedico = models.AutoField(primary_key=True) 
    paciente = models.OneToOneField(Paciente, null = True, blank = True, on_delete=models.CASCADE)
    estado_paciente = models.BooleanField()
    descripcion_paciente = models.CharField(max_length=50)
