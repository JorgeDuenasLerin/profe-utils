import django_tables2 as tables
import django_filters

from django.db import models
from django import forms

from .models import Incidencia
from django_filters import ChoiceFilter


class IncidenciaTable(tables.Table):
    class Meta:
        model = Incidencia
        fields = ('lugar',)
