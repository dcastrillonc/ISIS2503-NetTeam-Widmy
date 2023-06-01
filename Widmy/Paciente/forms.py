from django import forms
from .models import Paciente

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = [
            'id_Usuario',
            'nombre_Completo',
            'tipo_Identificacion',
            'identificacion',
            'email',
            'rol',
            'fecha_nacimiento', 
            'edad', 
            'genero', 
            'rh', 
            'plan', 
            'prioridad', 
        ]

        labels = {
            'id_Usuario': 'ID',
            'nombre_Completo': 'Nombre Completo',
            'tipo_Identificacion': 'Tipo de Identificacion',
            'identificacion': 'Identificación',
            'email': 'Email',
            'rol': 'Rol',
            'fecha_nacimiento': 'Fecha de Nacimiento', 
            'edad': 'Edad', 
            'genero': 'Genero', 
            'rh': 'RH', 
            'plan': 'Plan', 
            'prioridad': 'Prioridad',
        }