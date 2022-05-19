from django import forms
from django.forms import ModelForm
from .models import Usuario
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
        

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['Rut', 'Contra', 'Nombre', 'Apellidos','Mail','Telefono', 'Direccion'] 


class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()
	password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Confirma Contraseña', widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
		help_texts = {k:"" for k in fields }