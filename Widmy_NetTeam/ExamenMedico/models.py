from django.db import models

class ExamenMedico (models.Model):
    id_Examen_Medico = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    fecha_realizacion = models.DateField(null=True)
    resultado = models.CharField(max_length=1000)

    def __str__(self):
        return '{} - {} - {}'.format(self.nombre, self.tipo, self.resultado)