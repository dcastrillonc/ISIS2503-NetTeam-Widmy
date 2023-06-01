from django import forms
from .models import Profesional_Salud

class ProfesionalesForm(forms.ModelForm):
    class Meta:
        model = Profesional_Salud
        fields = [
            'id_Usuario',
            'nombre_Completo',
            'tipo_Identificacion',
            'identificacion',
            'email',
            'rol',
            'especialidad', 
            'sede', 
            'consultorio', 
        ]

        labels = {
            'id_Usuario': 'ID',
            'nombre_Completo': 'Nombre Completo',
            'tipo_Identificacion': 'Tipo de Identificacion',
            'identificacion': 'Identificación',
            'email': 'Email',
            'rol': 'Rol',
            'especialidad': 'Especialidad', 
            'sede': 'Sede', 
            'consultorio': 'Consultorio', 
        }