from tabnanny import verbose
from django.db import models

# Create your models here.

#Modelo para categoria
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id de categoria')
    nombreCategoria = models.CharField(max_length=50, verbose_name='Nombre de la Categoria')

    def __str__(self):
        return self.nombreCategoria

#Modelo para remedio

class Remedio(models.Model):
    id_remedio = models.CharField(max_length=20, verbose_name='Id remedio')
    nombreRemedio = models.CharField(max_length=50, verbose_name='Nombre remedio')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    precio = models.CharField(max_length=20, verbose_name='Precio remedio')
    marca =  models.CharField(max_length=20, verbose_name='Marca remedio')
    descripcion =  models.CharField(max_length=20, verbose_name='Descripcion remedio')
    
    def __str__(self):
        return self.nombreRemedio