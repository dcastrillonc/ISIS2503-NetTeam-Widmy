from django.db import models

class Profesional_Salud (models.Model):
    id_profesional_salud = models.CharField(max_length=10, primary_key=True)
    especialidad = models.CharField(max_length=35)
    sede = models.CharField(max_length=30)
    consultorio = models.CharField(max_length=20)

    def __str__(self):
        return '%s %s %s %s' % (self.id_profesional_salud, self.especialidad, self.sede, self.consultorio)
    
    
