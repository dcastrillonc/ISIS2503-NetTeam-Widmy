from django.db import models

class Historia_Clinica (models.Model):
    id_historia = models.CharField(max_length=10, primary_key=True)
    fechaCreacion_historia_clinica = models.CharField(max_length=50)
    fechaUltimaActualizacion_historia_clinica = models.CharField(max_length=50)
    descripcion_historia_clinica = models.CharField(max_length=2000)

    def __str__(self):
        #return '%s %s %s %s' % (self.id_historia, self.fechaCreacion_historia_clinica, self.fechaUltimaActualizacion_historia_clinica, self.descripcion_historia_clinica)
        return '{}'.format(self.id_historia)