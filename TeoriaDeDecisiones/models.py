from django.db import models


# Create your models here.

class Alternativa(models.Model):
    texto = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Consecuencia(models.Model):
    texto = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Lista():
    alternativas = []
    consecencias = []