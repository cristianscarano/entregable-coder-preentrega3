from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=40) # Nombre de la comision con 20 caracteres maximo
    comision = models.IntegerField() #numero de la comisión

class Estudiante(models.Model):
    nombre = models.CharField(max_length=30) # Nombre de la comision con 20 caracteres maximo
    apellido = models.CharField(max_length=30) #
    email = models.EmailField()

class Profesor(models.Model):
    nombre = models.CharField(max_length=30) # Nombre de la comision con 20 caracteres maximo
    apellido = models.CharField(max_length=30) #
    email = models.EmailField()
    profesion= models.CharField(max_length=20, null=True, blank= True)

class Entregables(models.Model):
    nombre = models.CharField(max_length=30) # Nombre de la comision con 20 caracteres maximo
    fecha_de_entrega = models.DateField()
    entregado = models.BooleanField()