from django.db import models

class Consulta (models.Model):
    sede = models.CharField(max_length=50)
    fecha = models.CharField(max_length=50)
    hora = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    completada = models.BooleanField()

    def __str__(self):
        return '%s %s %s %s' % (self.sede, self.fecha, self.hora, self.tipo)