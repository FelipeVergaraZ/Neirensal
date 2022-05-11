from rest_framework import serializers
from videojuego.models import Mercancia



class MercanciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mercancia
        fields = ['idproducto','nombreproducto','stockproducto','precioproducto','categoria','imagen']

