from django.urls import path
from django.urls import path, re_path, include
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import reverse_lazy
from . import views
from django.conf.urls import url
from .ajax import *

urlpatterns = [
	path('login/', views.login, name='login'),
	path('logout/', views.logout, name='logout'),
	    #Reestablecimiento de password
	path('reset/password_reset', PasswordResetView.as_view(template_name='users/password_reset_form.html', email_template_name="users/password_reset_email.html"), name = 'password_reset'),
    path('reset/password_reset_done', PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name = 'password_reset_done'),
    re_path(r'^reset/(?P<uidb64>[0-9A-za-z_\-]+)/(?P<token>.+)/$', PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name = 'password_reset_confirm'),
    path('reset/done',PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html') , name = 'password_reset_complete'),
	path('gestion_laboratoristas/', views.gestion_laboratorista, name='gestion_laboratorista'),
	path('gestion_minsal/', views.gestion_minsal, name='gestion_minsal'),
	path('eliminar-laboratorista/', views.eliminar_laboratorista, name='eliminar_laboratorista'),
	path('registrar-laboratorista/', views.registrar_laboratorista, name='registrar_laboratorista'),
	path('editar-laboratorista/', views.editar_laboratorista, name='editar_laboratorista'),
	path('eliminar-minsal', views.eliminar_minsal, name='eliminar_minsal'),
	path('registrar-minsal/', views.registrar_minsal, name='registrar_minsal'),
	path('editar-minsal/', views.editar_minsal, name='editar_minsal'),
	path('gestion_paciente/', views.gestion_paciente, name='gestion_paciente'),
	url(r'ajax/get_municipios', get_municipios, name='get_municipios'),
]