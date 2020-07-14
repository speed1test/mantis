from django.contrib import admin
from apps.covid.models import *

# Register your models here.

admin.site.register(Doctor)
admin.site.register(Laboratorista)
admin.site.register(Minsal)
admin.site.register(Departamento)
admin.site.register(Municipio)
admin.site.register(Paciente)
admin.site.register(CuadroMedico)
