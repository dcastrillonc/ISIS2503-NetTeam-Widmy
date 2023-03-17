from django.db import models

class Paciente (models.Model):
    id_paciente = models.CharField(max_length=10)
    fecha_nacimiento = models.CharField(max_length=15)
    edad = models.IntegerField()
    genero = models.CharField(max_length=20)
    rh = models.CharField(max_length=5)
    plan = models.CharField(max_length=40)
    prioridad = models.CharField(max_length=20)

    def __str__(self):
        return '%s %s %s %s %s %s' % (self.id_paciente, self.fecha_nacimiento, self.genero, self.rh, self.plan, self.prioridad)
    
    