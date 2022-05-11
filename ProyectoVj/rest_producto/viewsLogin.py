from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework.decorators import api_view , permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User 
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

@api_view(['POST'])
def login(request):
    data = JSONParser().parse(request)

    username = data['username'] #lo que esta entre comillas tiene que ser lo mismo que en el HTML
    password = data['password']
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response("Usuario inválido")
    #se valida la contraseña
    pass_valido = check_password(password, user.password)
    if not pass_valido:
        return Response("Password incorrecta")
    
    #crear o recuperar el token
    token, created = Token.objects.get_or_create(user=user)
    return Response(token.key)
