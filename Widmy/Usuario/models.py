from django.db import models

class Usuario (models.Model):
    id_Usuario = models.CharField(max_length=10, primary_key=True)
    nombre_Completo = models.CharField(max_length=100)
    tipo_Identificacion = models.CharField(max_length=50)
    identificacion = models.CharField(max_length=50)
    email = models.EmailField(blank=True)
    rol = models.CharField(max_length=50)

    class Meta:
        abstract = True

