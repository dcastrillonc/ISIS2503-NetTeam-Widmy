from django import forms
from .models import Antecedentes

class AntecedenteForm(forms.ModelForm):
    class Meta:
        model = Antecedentes
        fields = [
            'id_Antecedente', 
            'descripcion', 
        ]

        labels = {
            'id_Antecedente' : 'ID', 
            'descripcion': 'Descripción', 
        }