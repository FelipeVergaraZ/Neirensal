from django.shortcuts import render
from .models import Remedio
# Create your views here.

def home (request):
    remedios= Remedio.objects.all()
    datos = {
        'remedios': remedios
    }
    return render(request, 'core/home.html', datos) 