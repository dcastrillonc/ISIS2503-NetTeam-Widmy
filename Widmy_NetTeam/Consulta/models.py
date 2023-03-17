from django.db import models

class Consulta (models.Model):
    sede_consulta = models.CharField(max_length=50)
    fecha_consulta = models.CharField(max_length=50)
    hora_consulta = models.CharField(max_length=50)
    tipo_consulta = models.CharField(max_length=50)
    completada = models.BooleanField()

    def __str__(self):
        return '%s %s %s %s' % (self.sede_consulta, self.fecha_consulta, self.hora_consulta, self.tipo_consulta)