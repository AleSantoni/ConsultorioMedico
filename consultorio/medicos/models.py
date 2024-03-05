from django.db import models

from especialidades.models import Especialidades

# Create your models here.

class Medico(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    matricula = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.CharField(max_length=50)
    img=models.ImageField(upload_to='doctor' ,null=True, blank=True)
    especialidad = models.ManyToManyField(Especialidades)

    def __str__(self):
            return f'{self.nombre} {self.apellido}'