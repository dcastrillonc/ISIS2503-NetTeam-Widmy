from rest_framework import serializers
from . import models

class HistoriaClinicaSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id_Historia_Clinica', 'paciente', 'fecha_Creacion', 'fecha_Ultima_Actualizacion', 'descripcion', 'antecedentes', 'procedimientos', 'examen_Medico',)
        model = models.Historia_Clinica