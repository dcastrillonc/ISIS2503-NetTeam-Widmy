from django.db import models

class Antecedentes (models.Model):
    id_antecedente = models.CharField(max_length=10, primary_key=True)
    descripcion_antecedente = models.CharField(max_length=2000)

    def __str__(self):
        return '%s %s' % (self.id_antecedente, self.descripcion_antecedente)
    
    
