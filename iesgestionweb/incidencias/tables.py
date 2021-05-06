import django_tables2 as tables
import django_filters

from django.db import models
from django import forms

from .models import Incidencia, Respuesta
from django_filters import ChoiceFilter
from django.utils.html import format_html




class IncidenciaFilter(django_filters.FilterSet):
    class Meta:
        model = Incidencia
        fields = ['lugar']


class IncidenciaTable(tables.Table):
    respuesta = tables.Column(accessor='respuestas.all')

    def render_respuesta(self, value, record):
        text = ""
        for r in value:
            text += r.created_at.strftime('%Y-%m-%d %H:%M') + " - " + r.texto + "<br>"
        return format_html(text)

    class Meta:
        model = Incidencia
        fields = ("id", "texto", "respuesta", "lugar", "estado") # ""...")
