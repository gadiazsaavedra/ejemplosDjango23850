from django.db import models

# Create your models here.

class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()
    
class Jugador(models.Model):
    apellidos = models.CharField(max_length=40)
    edad = models.IntegerField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)