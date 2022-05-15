from django.db import models

# Create your models here.

class Producto(models.Model):
    id = models.AutoField(max_length=3, primary_key= True)
    nombre = models.CharField(max_length=64)
    categoria = models.CharField(max_length=32)
    precio = models.IntegerField()
    

    def __str__(self):
        return f'{self.nombre} -> {self.precio}'
