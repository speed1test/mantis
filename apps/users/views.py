from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib import messages
from .models import User
from django.core import mail
from apps.covid.models import *
from .forms import FormFiltrar

departamentos = Departamento.objects.all()
municipios = Municipio.objects.all()

def login(request):

	if(request.method == 'POST'):

		username = request.POST['username']
		password = request.POST['password']

		user = auth.authenticate(username=username,password=password)

		if user is not None:
			auth.login(request, user)
			return redirect('/')
		else:
			messages.error(request,'Credenciales inválidas')
			return redirect('/')

	else:
		return render(request,'users/login.html')
def logout(request):
	auth.logout(request)
	return redirect('/')

def gestion_laboratorista(request):	
	laboratoristas = Laboratorista.objects.all()
	contexto = {'laboratoristas': laboratoristas,}
	return render(request, 'gestion_usuarios/gestion_laboratorista.html', contexto)

def eliminar_laboratorista(request):

	Laboratorista.objects.filter(id=request.POST['id_delete']).delete()
	User.objects.filter(pk=request.POST['user_delete']).delete()

	return redirect('gestion_laboratorista')

def registrar_laboratorista(request):

	nombre = request.POST['nombre']
	apellido = request.POST['apellido']
	usuario = request.POST['usuario']
	correo = request.POST['correo']
	password = request.POST['password']
	password_2 = request.POST['password-2']
	dui = request.POST['telefono']
	direccion = request.POST['direccion']
	activo = True
	staff = True
	rol = 1

	user, laboratorista = User.objects.get_or_create(
		username = usuario,
		first_name = nombre,
		last_name = apellido,
		email = correo,
		password = password,
		dui = dui,
		direccion = direccion,
		rol = rol,
		is_active = activo,
		is_staff = staff
	)
	
	if laboratorista:
		user.set_password(password)
		user.save()

	covid_laboratorista = Laboratorista()

	covid_laboratorista.user = user

	covid_laboratorista.save()

	if request.user.is_authenticated:

		return redirect('gestion_laboratorista')

	else:
		
		return redirect('/')

def editar_laboratorista(request):

	laboratorista = Laboratorista.objects.get(pk=request.POST['id_edit'])

	laboratorista.user.first_name = request.POST['nombre_edit']
	laboratorista.user.last_name = request.POST['apellido_edit']
	laboratorista.user.username = request.POST['usuario_edit']
	laboratorista.user.email = request.POST['correo_edit']
	laboratorista.user.dui = request.POST['telefono_edit']
	laboratorista.user.direccion = request.POST['direccion_edit']
	laboratorista.user.save()
	laboratorista.save()

	return redirect('gestion_laboratorista')

def gestion_minsal(request):	
	minsal = Minsal.objects.all()
	contexto = {'minsal': minsal,}
	return render(request, 'gestion_usuarios/gestion_minsal.html', contexto)

def eliminar_minsal(request):

	Minsal.objects.filter(id=request.POST['id_delete']).delete()
	User.objects.filter(pk=request.POST['user_delete']).delete()

	return redirect('gestion_minsal')

def registrar_minsal(request):

	nombre = request.POST['nombre']
	apellido = request.POST['apellido']
	usuario = request.POST['usuario']
	correo = request.POST['correo']
	password = request.POST['password']
	password_2 = request.POST['password-2']
	dui = request.POST['telefono']
	direccion = request.POST['direccion']
	activo = True
	staff = True
	rol = 2

	user, minsal = User.objects.get_or_create(
		username = usuario,
		first_name = nombre,
		last_name = apellido,
		email = correo,
		password = password,
		dui = dui,
		direccion = direccion,
		rol = rol,
		is_active = activo,
		is_staff = staff
	)
	
	if minsal:
		user.set_password(password)
		user.save()

	covid_minsal = Minsal()

	covid_minsal.user = user

	covid_minsal.save()

	if request.user.is_authenticated:

		return redirect('gestion_minsal')

	else:
		
		return redirect('/')

def editar_minsal(request):

	minsal = Minsal.objects.get(pk=request.POST['id_edit'])

	minsal.user.first_name = request.POST['nombre_edit']
	minsal.user.last_name = request.POST['apellido_edit']
	minsal.user.username = request.POST['usuario_edit']
	minsal.user.email = request.POST['correo_edit']
	minsal.user.dui = request.POST['telefono_edit']
	minsal.user.direccion = request.POST['direccion_edit']
	minsal.user.save()
	minsal.save()

	return redirect('gestion_minsal')

def gestion_paciente(request):	
	pacientes = CuadroMedico.objects.all()
	form = FormFiltrar()
	contexto = {'pacientes': pacientes,'form':form,}
	return render(request, 'gestion_usuarios/gestion_paciente.html', contexto)


