from django import forms
from .models import ExamenMedico

class ExamenMedicoForm(forms.ModelForm):
    class Meta:
        model = ExamenMedico
        fields = [
            'id_Examen_Medico', 
            'nombre', 
            'tipo',
            'fecha_realizacion',
            'resultado',
        ]

        labels = {
            'id_Examen_Medico' : 'ID', 
            'nombre': 'Nombre del Examen', 
            'tipo': 'Tipo del Examen', 
            'fecha_realizacion': 'Fecha de Realización', 
            'resultado': 'Resultado', 
        }