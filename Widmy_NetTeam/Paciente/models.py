from django.db import models

from Usuario.models import Usuario

class Paciente (Usuario):
    fecha_nacimiento = models.CharField(max_length=15)
    edad = models.IntegerField()
    genero = models.CharField(max_length=20)
    rh = models.CharField(max_length=5)
    plan = models.CharField(max_length=40)
    prioridad = models.CharField(max_length=20)

    def __str__(self):
        return '{} - {} {}'.format(self.nombre_Completo, self.tipo_Identificacion, self.identificacion)
    