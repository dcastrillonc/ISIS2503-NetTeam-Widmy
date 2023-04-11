from django.db import models

class Procedimientos (models.Model):
    id_Procedimiento = models.CharField(max_length=10, primary_key=True)
    tipo_de_Procedimiento = models.CharField(max_length=50)
    fecha = models.CharField(max_length=25)
    descripcion = models.CharField(max_length=2000)

    def __str__(self):
        return '{} - {}'.format(self.tipo_de_Procedimiento, self.descripcion)