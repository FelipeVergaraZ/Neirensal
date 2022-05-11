from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from rest_framework import status

from rest_framework.decorators import api_view

from rest_framework.response import Response

from rest_framework.parsers import JSONParser

from django.views.decorators.csrf import csrf_exempt

from videojuego.models import Mercancia

from .serializers import MercanciaSerializer



@csrf_exempt

@api_view(['GET','POST'])

def lista_mercancia(request):

    if request.method == 'GET':
        
        mercancia = Mercancia.objects.all()

        serializer = MercanciaSerializer(mercancia, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':

        data = JSONParser().parse(request)

        serializer = MercanciaSerializer(data=data)

        if(serializer.is_valid()):

            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def detalle_categoria(request,id):
    try:
        mercancia = Mercancia.objects.get(ID_PROD=id)
    except Mercancia.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = MercanciaSerializer(mercancia)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = MercanciaSerializer(mercancia,data=data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        mercancia.delete()
        return Response(status=status.HTTP_204_NOT_CONTENT)  