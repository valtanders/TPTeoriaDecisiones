from django.db import models


# Create your models here.

class Alternativas(models.Model):
    texto = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Consecuencias(models.Model):
    texto = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
