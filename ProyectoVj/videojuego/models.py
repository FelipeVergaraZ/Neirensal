from django.db import models


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

class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True,verbose_name='Id de Categoria')
    nombreCategoria= models.CharField(max_length=50,verbose_name='Nombre deL Categoria')

    def __str__(self):
        return self.nombreCategoria


class Mercancia(models.Model):
    idproducto=models.IntegerField(primary_key=True,verbose_name='Id del Producto')
    nombreproducto=models.CharField(max_length=20,verbose_name='Nombre del Producto')
    stockproducto=models.IntegerField(verbose_name='Stock del producto')
    precioproducto=models.IntegerField(verbose_name='Precio del producto')
    imagen=models.ImageField(upload_to='Imagenes',null=True)
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombreproducto


