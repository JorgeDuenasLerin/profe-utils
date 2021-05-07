from django import forms
from .models import Lugar, Acceso, Incidencia

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_pass(value):
    actual = Acceso.objects.latest('fecha')
    if value != actual.clave:
        raise ValidationError(
            'La contraseña ' + value + ' no es correcta',
            params={'value': value},
        )

class IncidenciaForm(forms.ModelForm):
    secreto = forms.CharField(label='Contraseña',
                    widget=forms.TextInput(attrs={'placeholder': 'Secreto...'}),
                    validators=[validate_pass]
            )

    class Meta:
        model = Incidencia
        fields = ['lugar', 'texto']
        labels = {
            'lugar': 'Aula',
            'texto': 'Texto',
            'secreto': 'Contraseña'
        }
