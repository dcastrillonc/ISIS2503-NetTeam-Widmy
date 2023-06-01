from django import forms
from .models import Procedimientos

class ProcedimientosForm(forms.ModelForm):
    class Meta:
        model = Procedimientos
        fields = [
            'id_Procedimiento',
            'tipo_de_Procedimiento',
            'fecha',
            'descripcion',
     
        ]

        labels = {
            'id_Procedimiento': 'ID',
            'tipo_de_Procedimiento': 'Tipo de Procedimiento',
            'fecha': 'Fecha del Procedimiento',
            'descripcion': 'Descipción',
        }