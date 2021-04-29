from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Lugar, Incidencia, Respuesta, Acceso
from .tables import IncidenciaTable, IncidenciaFilter
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

class IncidenciaListView(SingleTableMixin, FilterView):

    model = Incidencia
    table_class = IncidenciaTable
    template_name = 'incidencias/index.html'

    filterset_class = IncidenciaFilter

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)

        try:
            lugar_id = int(self.request.GET.get('lugar', ''))
        except:
            lugar_id = 0
        lugar_selected = Lugar.objects.filter(pk=lugar_id).first()
        lugar_text = "Todas" if lugar_selected is None else lugar_selected.lugar

        context['lugar_selected'] = lugar_selected
        context['lugar_text'] = lugar_text
        context['lugares'] = Lugar.objects.all()

        return context
