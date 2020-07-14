# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User
from apps.covid.models import Municipio, Departamento


class UserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'rol', 'direccion')

class UserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'rol', 'direccion')

class FormFiltrar(forms.Form):

    departamento = forms.ModelChoiceField(
        label=u'', 
        queryset=Departamento.objects.all(),
        widget=forms.Select(attrs={'class':'form-control'}),
    )
    
    municipio = forms.ModelChoiceField(
        label=u'', 
        queryset=Municipio.objects.all(),
        widget=forms.Select(attrs={'class':'form-control'}),
    )
