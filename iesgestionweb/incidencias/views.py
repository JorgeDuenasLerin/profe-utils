from django.shortcuts import render
from django.http import HttpResponse
from .models import Lugar, Incidencia, Respuesta, Acceso

def index(request, lugar_id=None):
    context = {
        'lugar_id': lugar_id,
        'lugares': Lugar.objects.all(),
        'incidencias': Incidencia.objects.all()
    }
    return render(request, 'incidencias/index.html', context)
