from django.db import models

# Create your models here.
class Lenguaje(models.Model):
    idLenguaje = models.AutoField(primary_key=True)
    nombreLenguaje = models.CharField(max_length=200)
    complejidad = models.IntegerField()
    status = models.IntegerField()

class PruebaTecnica(models.Model):
    idPruebaTecnica = models.AutoField(primary_key=True)
    nombrePrueba = models.CharField(max_length=200)
    lenguaje = models.ForeignKey(Lenguaje, related_name='pruebas', on_delete=models.CASCADE)
    status = models.IntegerField()

class PruebaTecnicaPregunta(models.Model):
    idPruebaPregunta = models.AutoField(primary_key=True)
    pruebaPregunta = models.CharField(max_length=200)
    pruebaReferencia = models.ForeignKey(PruebaTecnica,related_name='pregunta', on_delete=models.CASCADE)
    status = models.IntegerField()

class PruebaTecnicaRespuesta(models.Model):
    idPruebaRespuesta = models.AutoField(primary_key=True)
    respuesta = models.CharField(max_length=200)
    idPregunta = models.ForeignKey(PruebaTecnicaPregunta, related_name='respuesta', on_delete=models.CASCADE)
    esValido = models.IntegerField()