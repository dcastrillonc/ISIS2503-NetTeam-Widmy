from django.db import models

class Paciente (models.Model):
    id_paciente = models.CharField(max_length=10)
    fecha_nacimiento_paciente = models.CharField(max_length=15)
    edad_paciente = models.IntegerField()
    genero_paciente = models.CharField(max_length=20)
    rh_paciente = models.CharField(max_length=5)
    plan_paciente = models.CharField(max_length=40)
    prioridad_paciente = models.CharField(max_length=20)

    def __str__(self):
        return '%s %s %s %s %s %s' % (self.id_paciente, self.fecha_nacimiento_paciente, self.genero_paciente, self.rh_paciente, self.plan_paciente, self.prioridad_paciente)
    
    