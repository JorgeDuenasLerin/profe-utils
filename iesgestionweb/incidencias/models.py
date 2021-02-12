from django.db import models
from datetime import datetime
# Create your models here.

class Acceso(models.Model):
    clave = models.CharField(max_length=200)
    fecha = models.DateTimeField('Desde')

    def __str__(self):
        return self.clave

class Incidencia(models.Model):
    lugar = models.CharField(max_length=200)
    texto = models.TextField()
    ESTADOS = [
        ('A', 'Abierta'),
        ('C', 'Cerrada'),
        ('P', 'SinSolución'),
    ]
    estado = models.CharField(
        max_length=2,
        choices=ESTADOS,
        default='A',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.lugar + ' ' + self.estado + ' ' + self.created_at.strftime('%Y-%m-%d %H:%M')

class Respuesta(models.Model):
    incidencia = models.ForeignKey(Incidencia, on_delete=models.CASCADE)
    texto = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.incidencia.lugar + ' - ' + self.updated_at.strftime('%Y-%m-%d %H:%M')
