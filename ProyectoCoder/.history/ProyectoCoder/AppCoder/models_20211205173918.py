from django.db import models

# Create your models here.

class Curso(models.Model):
    nombre = models.CharField()
    camada = models.IntegerField()