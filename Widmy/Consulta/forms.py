from django import forms
from .models import Consulta

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = [
            'paciente', 
            'profesional_Salud', 
            'historia_Clinica', 
            'sede_Consulta', 
            'fecha_Consulta', 
            'hora_Consulta', 
            'tipo_Consulta', 
            'completada',
        ]

        labels = {
            'paciente' : 'Paciente', 
            'profesional_Salud': 'Profesional de la Salud', 
            'historia_Clinica': 'Historia Clínica', 
            'sede_Consulta': 'Sede', 
            'fecha_Consulta': 'Fecha de la Consulta', 
            'hora_Consulta': 'Hora de la Consulta', 
            'tipo_Consulta': 'Tipo de Consulta', 
            'completada': 'Completada',
        }