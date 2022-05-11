from rest_framework import serializers
from videojuego.models import Categoria



class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['idCategoria','nombreCategoria']

