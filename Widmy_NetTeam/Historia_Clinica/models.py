from django.db import models

class Historia_Clinica (models.Model):
    id_historia = models.CharField(max_length=10, primary_key=True)
    fechaCreacion = models.CharField(max_length=50)
    fechaUltimaActualizacion = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=2000)

    def __str__(self):
        return '%s %s %s %s' % (self.id_historia, self.fechaCreacion, self.fechaUltimaActualizacion, self.descripcion)