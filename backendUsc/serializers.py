from rest_framework import serializers 
from backendUsc.models import *

class languageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lenguaje
        fields = ('idLenguaje',
                  'nombreLenguaje',
                  'complejidad',
                  'status')

class pruebaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PruebaTecnica
        fields = ('idPruebaTecnica',
                  'nombrePrueba',
                  'lenguaje',
                  'status')

class preguntaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PruebaTecnicaPregunta
        fields = ('idPruebaPregunta',
                  'pruebaPregunta',
                  'pruebaReferencia',
                  'status')

class respuestaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PruebaTecnicaRespuesta
        fields = ('idPruebaRespuesta',
                  'respuesta',
                  'idPregunta',
                  'esValido')

class reservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = ('idReserva',
                  'fechaInicio',
                  'usuarioReserva',
                  'fechaFin',
                  'cantidadPersonas')