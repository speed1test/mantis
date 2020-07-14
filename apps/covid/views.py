from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.contrib import messages
from django.urls import reverse_lazy
from datetime import date, datetime
from apps.covid.models import *

def index(request):
	return render(request, 'index.html')

# Create your views here.
