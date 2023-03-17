from django.db import models

class Profesional_Salud (models.Model):
    id_profesional_salud = models.CharField(max_length=10, primary_key=True)
    especialidad_profesional_salud = models.CharField(max_length=35)
    sede_profesional_salud = models.CharField(max_length=30)
    consultorio_profesional_salud = models.CharField(max_length=20)

    def __str__(self):
        return '%s %s %s %s' % (self.id_profesional_salud, self.especialidad_profesional_salud, self.sede_profesional_salud, self.consultorio_profesional_salud)
    
    
