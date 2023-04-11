from django.db import models

class Antecedentes (models.Model):
    id_Antecedente = models.CharField(max_length=10, primary_key=True)
    descripcion = models.CharField(max_length=2000)

    def __str__(self):
        return '%s' % (self.descripcion)
    
    
