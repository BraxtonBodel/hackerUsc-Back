from django.shortcuts import render


from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from backendUsc.models import Lenguaje, PruebaTecnica, PruebaTecnicaPregunta, Reserva, Usuario
from backendUsc.serializers import *
from rest_framework.decorators import api_view


# Create your views here.
@api_view(['GET', 'POST', 'DELETE'])
def languages_list(request):
    # GET list of backendUsc, POST a new tutorial, DELETE all backendUsc
    language = Lenguaje.objects.filter(status=True)
        
    if request.method == 'GET': 
        hackerUsc_serializer = languageSerializer(language, many=True)
        return JsonResponse(hackerUsc_serializer.data, safe=False)

# Create your views here.
@api_view(['GET', 'POST', 'DELETE'])
def testPerLanguage(request, pk):
    # GET list of backendUsc, POST a new tutorial, DELETE all backendUsc
    if request.method == 'GET':
        language = Lenguaje.objects.get(pk=pk)
        prueba = language.pruebas.all()
        hackerSerializer = pruebaSerializer(prueba,many=True) 
        return JsonResponse(hackerSerializer.data,safe=False) 

# Create your views here.
@api_view(['GET', 'POST', 'DELETE'])
def questionPerTest(request, pk):
    # GET list of backendUsc, POST a new tutorial, DELETE all backendUsc
    if request.method == 'GET':
        prueba = PruebaTecnica.objects.get(pk=pk)
        questions = prueba.pregunta.all()
        hackerSerializer = preguntaSerializer(questions,many=True) 
        return JsonResponse(hackerSerializer.data,safe=False)

@api_view(['GET', 'POST', 'DELETE'])
def answerPerQuestion(request, pk):
    # GET list of backendUsc, POST a new tutorial, DELETE all backendUsc
    if request.method == 'GET':
        pregunta = PruebaTecnicaPregunta.objects.get(pk=pk)
        respuesta = pregunta.respuesta.all()
        hackerSerializer = respuestaSerializer(respuesta,many=True) 
        return JsonResponse(hackerSerializer.data,safe=False)

@api_view(['GET', 'POST', 'DELETE'])
def insertTest(request ):
    # GET list of backendUsc, POST a new tutorial, DELETE all backendUsc
    testData = JSONParser().parse(request)
    prueba_serializer = pruebaSerializer(data=testData)
    if prueba_serializer.is_valid():
        prueba_serializer.save()
        return JsonResponse(prueba_serializer.data, status=status.HTTP_201_CREATED) 
    return JsonResponse(prueba_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST', 'DELETE'])
def getReservation(request, pk):
    # GET list of backendUsc, POST a new tutorial, DELETE all backendUsc
    # GET list of backendUsc, POST a new tutorial, DELETE all backendUsc
    if request.method == 'GET':
        usuario = Usuario.objects.get(pk=pk)
        reserva = usuario.reserva.all()
        hackerSerializer = reservaSerializer(reserva,many=True) 
        return JsonResponse(hackerSerializer.data,safe=False)                
