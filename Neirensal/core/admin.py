from django.contrib import admin
from .models import Producto, Categoria, Paciente

# Register your models here.

admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(Paciente)