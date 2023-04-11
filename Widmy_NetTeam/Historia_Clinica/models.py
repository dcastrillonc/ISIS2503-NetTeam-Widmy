from django.db import models

from Paciente.models import Paciente
from Antecedentes.models import Antecedentes
from Procedimientos.models import Procedimientos
from ExamenMedico.models import ExamenMedico

class Historia_Clinica (models.Model):
    id_Historia_Clinica = models.CharField(max_length=10)
    paciente = models.OneToOneField(Paciente, on_delete=models.CASCADE, primary_key=True)
    fecha_Creacion = models.CharField(max_length=50)
    fecha_Ultima_Actualizacion = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=2000)
    antecedentes = models.ForeignKey(Antecedentes, on_delete=models.CASCADE, default=None)
    procedimientos = models.ForeignKey(Procedimientos, on_delete=models.CASCADE, default=None)
    examen_Medico = models.ForeignKey(ExamenMedico, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return '{}'.format(self.paciente)