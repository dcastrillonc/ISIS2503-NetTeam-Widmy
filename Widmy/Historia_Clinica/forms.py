from django import forms
from .models import Historia_Clinica

class HistoriaClinicaForm(forms.ModelForm):
    class Meta:
        model = Historia_Clinica
        fields = [
            'id_Historia_Clinica', 
            'paciente', 
            'fecha_Creacion', 
            'fecha_Ultima_Actualizacion', 
            'descripcion', 
            'antecedentes', 
            'procedimientos', 
            'examen_Medico',
        ]

        labels = {
            'id_Historia_Clinica': 'ID', 
            'paciente': 'Paciente', 
            'fecha_Creacion': 'Fecha de Creación', 
            'fecha_Ultima_Actualizacion': 'Fecha Última Actualización', 
            'descripcion': 'Descripción', 
            'antecedentes': 'Antecedentes', 
            'procedimientos': 'Procedimientos', 
            'examen_Medico': 'Examenes Médicos',
        }