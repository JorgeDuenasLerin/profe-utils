from django.contrib import admin

# Register your models here.

from .models import Acceso, Lugar, Incidencia, Respuesta

admin.site.register(Acceso)
admin.site.register(Lugar)
admin.site.register(Respuesta)


class RespuestaInline(admin.TabularInline):
    model = Respuesta
    extra = 1


class IncidenciaAdmin(admin.ModelAdmin):
    inlines = [RespuestaInline]

admin.site.register(Incidencia, IncidenciaAdmin)
