# Generated by Django 3.2 on 2021-05-07 08:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('incidencias', '0002_auto_20210426_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incidencia',
            name='estado',
            field=models.CharField(choices=[('A', 'Abierta'), ('C', 'Cerrada')], default='R', max_length=2),
        ),
        migrations.AlterField(
            model_name='respuesta',
            name='incidencia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='respuestas', to='incidencias.incidencia'),
        ),
    ]
