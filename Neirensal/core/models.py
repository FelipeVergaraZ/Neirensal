
from tabnanny import verbose

from django.db import models

# Create your models here.

#Modelo para categoria
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id de categoria')
    nombreCategoria = models.CharField(max_length=50, verbose_name='Nombre de la Categoria')

    def __str__(self):
        return self.nombreCategoria


class Producto(models.Model):
    id = models.AutoField(max_length=3, primary_key= True)
    nombre = models.CharField(max_length=64)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    precio = models.IntegerField()
    stock = models.CharField(max_length=20, verbose_name='Stock')
    marca =  models.CharField(max_length=20, verbose_name='Laboratorio')
    descripcion =  models.CharField(max_length=20, verbose_name='Descripcion remedio')
    estado =  models.CharField(max_length=20, verbose_name='Estado del remedio')

    def __str__(self):
        return f'{self.nombre} -> {self.precio}'

class Paciente(models.Model):
    nombre = models.CharField(max_length=64)
    correo = models.CharField(max_length=64, verbose_name='Correo')
    numero = models.CharField(max_length=64, verbose_name='Numero')
    diagnostico = models.CharField(max_length=40, verbose_name='Diagnostico paciente')

    def __str__(self):
        return self.nombre


#Modelo para remedio