from tabnanny import verbose

from django.db import models

# Create your models here.

class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id de categoria')
    nombreCategoria = models.CharField(max_length=50, verbose_name='Nombre de la Categoria')

    def __str__(self):
        return self.nombreCategoria

class Producto(models.Model):
    id = models.AutoField(max_length=3, primary_key= True)
    nombre = models.CharField(max_length=64)
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)
    precio = models.IntegerField()
    stock = models.CharField(max_length=20, verbose_name='Stock')
    marca =  models.CharField(max_length=20, verbose_name='Laboratorio')
    descripcion =  models.CharField(max_length=20, verbose_name='Descripcion remedio')
    estado =  models.CharField(max_length=20, verbose_name='Estado del remedio')

    def __str__(self):
        return f'{self.nombre} -> {self.precio}'

class Rango(models.Model):
    idRango = models.IntegerField(primary_key=True,verbose_name='Id de Rango')
    nombreRango= models.CharField(max_length=50,verbose_name='Nombre deL Rango')

    def __str__(self):
        return self.nombreRango


class Usuario(models.Model):
    Rut = models.CharField(max_length=9,primary_key=True, verbose_name='Rut ')
    Contra = models.CharField(max_length=20,verbose_name='Contraseña')
    Nombre = models.CharField(max_length=30,verbose_name='Nombre')
    Apellidos = models.CharField(max_length=60,verbose_name='Apellidos')
    Mail = models.CharField(max_length=100,verbose_name='Mail')
    Telefono = models.IntegerField(verbose_name='Teléfono')
    Direccion = models.CharField(max_length=300,verbose_name='Dirección')

    def __str__(self):
        return self.Rut

#Modelo para remedio