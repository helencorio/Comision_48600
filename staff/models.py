from django.db import models

# Create your models here.

class Persona:
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=20)
    correo = models.EmailField()

class ProfesYTutores(models.Model, Persona):
    pass

class OtrosEmpleados(models.Model, Persona):
    pass