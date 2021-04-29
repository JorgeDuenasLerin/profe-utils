import django_tables2 as tables
import django_filters
from .models import Incidencia


class IncidenciaFilter(django_filters.FilterSet):
    class Meta:
        model = Incidencia
        fields = ['lugar', 'estado']

class IncidenciaTable(tables.Table):
    class Meta:
        model = Incidencia
