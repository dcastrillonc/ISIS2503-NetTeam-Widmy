from django.db import models

class Procedimientos (models.Model):
    id_procedimiento = models.CharField(max_length=10, primary_key=True)
    tipo_procedimiento = models.CharField(max_length=50)
    fecha_procedimiento = models.CharField(max_length=25)
    descripcion_procedimiento = models.CharField(max_length=2000)

    def __str__(self):
        return '%s %s %s %s' % (self.id_procedimiento, self.tipo_procedimiento, self.fecha_procedimiento, self.descripcion_procedimiento)
    
    
