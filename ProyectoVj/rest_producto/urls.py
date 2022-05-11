from django.urls import path

from rest_producto.views import lista_mercancia
from rest_producto.viewsLogin import login



urlpatterns = [

    path('lista_mercancia',lista_mercancia,name='lista_mercancia'),
    
]


