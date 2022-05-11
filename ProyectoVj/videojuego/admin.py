from django.contrib import admin
from .models import Categoria, Rango,Usuario,Mercancia

# Register your models here.
admin.site.register(Rango)
admin.site.register(Usuario)
admin.site.register(Categoria)
admin.site.register(Mercancia)