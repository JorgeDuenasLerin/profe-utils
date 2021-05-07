from django.contrib import admin

# Register your models here.

from .models import Acceso, Lugar, Incidencia, Respuesta

admin.site.register(Acceso)
admin.site.register(Lugar)
admin.site.register(Respuesta)


class RespuestaInline(admin.TabularInline):
    model = Respuesta
    extra = 0


class IncidenciaAdmin(admin.ModelAdmin):
    inlines = [RespuestaInline]
    list_display = ('id', 'lugar', 'texto', 'estado', 'created_at')
    list_filter = ('estado', 'lugar')
    date_hierarchy = 'created_at'

admin.site.register(Incidencia, IncidenciaAdmin)
