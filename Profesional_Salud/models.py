from django.db import models

from Usuario.models import Usuario

class Profesional_Salud (Usuario):
    especialidad = models.CharField(max_length=35)
    sede = models.CharField(max_length=30)
    consultorio = models.CharField(max_length=20)

    def __str__(self):
        return '{} - {}'.format(self.nombre_Completo, self.especialidad)
    
