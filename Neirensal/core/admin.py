from django.contrib import admin
from .models import Paciente, Producto, Categoria

# Register your models here.

admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(Paciente)
