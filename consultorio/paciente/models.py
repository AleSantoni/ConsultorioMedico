from django.db import models

# Create your models here.

class Paciente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.IntegerField()
    fecha_nacimiento = models.DateField( auto_now=False, auto_now_add=False)
    telefono = models.IntegerField( )
    email = models.EmailField()
    direccion = models.CharField(max_length=100)
    observaciones = models.TextField(max_length=200)

    def __str__(self):
        return self.nombre