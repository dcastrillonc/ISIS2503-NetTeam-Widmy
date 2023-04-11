from django.db import models

from Paciente.models import Paciente
from Historia_Clinica.models import Historia_Clinica
from Profesional_Salud.models import Profesional_Salud

class Consulta (models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, default=None)
    profesional_Salud = models.ForeignKey(Profesional_Salud, on_delete=models.CASCADE, default=None)
    historia_Clinica = models.ForeignKey(Historia_Clinica, on_delete=models.CASCADE, default=None)
    sede_Consulta = models.CharField(max_length=50)
    fecha_Consulta = models.DateField(null=True)
    hora_Consulta = models.CharField(max_length=50)
    tipo_Consulta = models.CharField(max_length=50)
    completada = models.BooleanField()

    def __str__(self):
        return '{}'.format(self.paciente)