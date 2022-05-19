from pyexpat import model
from django import forms
from django.forms import ModelForm
from .models import Producto, Paciente

class ProductoForm(ModelForm):


    class Meta:
        model = Producto
        fields =['id','nombre','categoria','precio','stock','marca','descripcion','estado']

class PacienteForm(ModelForm):

    class Meta:
        model = Paciente
        fields = ['nombre','correo','numero', 'diagnostico']