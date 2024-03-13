from django.db import models
from especialidades.models import Especialidades
from medicos.models import Medicos
from paciente.models import Pacientes

# Create your models here.

class Turnos(models.Model):
    especialidad= models.ForeignKey(Especialidades, on_delete=models.CASCADE)
    medico= models.ForeignKey(Medicos, on_delete=models.CASCADE)
    fecha= models.DateField()
    hora= models.TimeField()
    paciente= models.ForeignKey(Pacientes, on_delete=models.CASCADE)
    observaciones= models.TextField()
    

    def __str__(self):
        return self.nombre
    
class Disponibilidad(models.Model):
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    dia_semana = models.CharField(max_length=10, choices=[
        ('lunes', 'Lunes'),
        ('martes', 'Martes'),
        ('miercoles', 'Miércoles'),
        ('jueves', 'Jueves'),
        ('viernes', 'Viernes'),
        ('sabado', 'Sábado'),
    ])
    horarios = models.ManyToManyField('Horario', blank=True)

    def __str__(self):
        return f"{self.medico} - {self.dia_semana} - {', '.join(str(h) for h in self.horarios.all())}"

class Horario(models.Model):
    hora = models.TimeField()

    def __str__(self):
        return str(self.hora)