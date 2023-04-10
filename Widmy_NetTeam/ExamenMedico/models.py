from django.db import models

class ExamenMedico (models.Model):
    id_examenMedico = models.CharField(max_length=10, primary_key=True)
    nombre_examenMedico = models.CharField(max_length=50)
    tipo_examenMedico = models.CharField(max_length=50)
    fecha_examenMedico = models.DateField(null=True)
    resultado_examenMedico = models.CharField(max_length=1000)

    def __str__(self):
        return '%s %s %s %s' % (self.id_examenMedico, self.nombre_examenMedico, self.tipo_examenMedico, self.resultado_examenMedico)
