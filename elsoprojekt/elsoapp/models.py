from django.db import models

# Create your models here.

class Tanulo(models.Model):
    nev = models.CharField(max_length=128)
    felnev = models.CharField(max_length=128)
    jelszo = models.CharField(max_length=128)
    email = models.CharField(max_length=128)

class Foglalkozas(models.Model):
    nev = models.CharField(max_length=128)

class Valasztas(models.Model):
    tanulo = models.ForeignKey(Tanulo, on_delete=models.CASCADE)
    Foglalkozas = models.ForeignKey(Foglalkozas, on_delete=models.CASCADE)
