from rest_framework import serializers 
from backendUsc.models import Lenguaje, PruebaTecnica, PruebaTecnicaPregunta, PruebaTecnicaRespuesta

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