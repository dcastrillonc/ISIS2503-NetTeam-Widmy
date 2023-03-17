from django.db import models

class Usuario (models.Model):
    id_usuario = models.CharField(max_length=10, primary_key=True)
    nombre_completo_usuario = models.CharField(max_length=50)
    tipo_identificacion_usuario = models.CharField(max_length=50)
    identificacion_usuario = models.CharField(max_length=50)
    email_usuario = models.CharField(max_length=50)
    rol_usuario = models.CharField(max_length=50)

    def __str__(self):
        return '%s %s %s %s %s %s' % (self.id_usuario,self.nombre_completo_usuario, self.tipo_identificacion_usuario, self.identificacion_usuario, self.email_usuario, self.rol_usuario)
    

