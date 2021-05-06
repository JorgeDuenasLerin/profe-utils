from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Lugar, Incidencia, Respuesta, Acceso
from .tables import IncidenciaTable
from django_tables2.views import SingleTableView

from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin




"""
class FilteredPersonListView(SingleTableMixin, FilterView):
    table_class = PersonTable
    model = Person
    template_name = "template.html"

    filterset_class = PersonFilter
"""

class IncidenciaListView(SingleTableView):

    model = Incidencia
    table_class = IncidenciaTable
    template_name = 'incidencias/index.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)

        incidencias = Lugar.objects.all()

        try:
            lugar_id = int(self.request.GET.get('lugar', ''))
            incidencias = incidencias.filter(pk=lugar_id)
        except:
            lugar_id = 0

        context['lugares'] = Lugar.objects.all()

        return context
