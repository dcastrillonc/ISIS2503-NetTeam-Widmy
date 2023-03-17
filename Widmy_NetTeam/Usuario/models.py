from django.db import models

class Usuario (models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    nombre_completo = models.CharField(max_length=50)
    tipo_identificacion = models.CharField(max_length=50)
    identificacion = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    rol = models.CharField(max_length=50)

    def __str__(self):
        return '%s %s %s %s %s %s' % (self.id,self.nombre_completo, self.tipo_identificacion, self.identificacion, self.email, self.rol)
    

