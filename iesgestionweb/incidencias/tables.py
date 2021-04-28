import django_tables2 as tables
from .models import Incidencia

class IncidenciaTable(tables.Table):
    class Meta:
        model = Incidencia
