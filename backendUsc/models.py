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

class Usuario(models.Model):
    identificacionUsuario = models.IntegerField(primary_key=True)
    nombreUsuario = models.CharField(max_length=200)
    apellidoUsuario = models.CharField(max_length=200)
    edad = models.IntegerField()
    correoUsuario = models.CharField(max_length=200)
    facultad = models.CharField(max_length=200)

class Reserva(models.Model):
    idReserva = models.AutoField(primary_key=True)
    fechaInicio = models.DateField()
    usuarioReserva = models.ForeignKey(Usuario, related_name='reserva', on_delete=models.CASCADE)
    fechaFin = models.DateField()
    cantidadPersonas = models.IntegerField()