from django.shortcuts import render
from django.http import HttpResponse
from .models import Lugar, Incidencia, Respuesta, Acceso

def index(request):
    try:
        lugar_id = int(request.GET.get('lugar', ''))
    except:
        lugar_id = 0
    lugar_selected = Lugar.objects.filter(pk=lugar_id).first()
    lugar_text = "Todas" if lugar_selected is None else lugar_selected.lugar

    context = {
        'lugar_selected': lugar_selected,
        'lugar_text': lugar_text,
        'lugares': Lugar.objects.all(),
        'incidencias': Incidencia.objects.all()
    }
    return render(request, 'incidencias/index.html', context)
