from django.db import models

# Create your models here.

class Eventos(models.Model):

    nome = models.CharField(max_length=80)
    tema = models.CharField(max_length=80)
    descricao = models.CharField(max_length=5000)
    data = models.DateField
    hora = models.TimeField
    organizador = models.CharField(max_length=80)
    telefone = models.CharField(max_length=15)
    email = models.EmailField

def __str__(self):

    return self.nome