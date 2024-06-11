from django.db import models

# Create your models here.
class Carros(models.Model):
    modelo = models.CharField(max_length=100)
    marca = models.CharField(max_length=150)
    ano = models.IntegerField()