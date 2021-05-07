from django import forms
from .models import Lugar, Acceso

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_pass(value):
    actual = Acceso.objects.latest('fecha')
    if value != actual.clave:
        raise ValidationError(
            'La contraseña ' + value + ' no es correcta',
            params={'value': value},
        )

class IncidenciaForm(forms.Form):
    secreto = forms.CharField(label='pass',
                    widget=forms.TextInput(attrs={'placeholder': 'Secreto...'}),
                    validators=[validate_pass]
            )
    lugar = forms.ModelChoiceField(queryset=Lugar.objects.all(), empty_label="(Selecciona aula)")
    texto = forms.CharField(widget=forms.Textarea)
