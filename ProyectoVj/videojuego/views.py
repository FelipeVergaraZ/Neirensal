from django.core import paginator
from .models import *
from django.shortcuts import render, redirect, get_object_or_404
from .models import Mercancia, Usuario
from django import forms

from .forms import MercanciaForm
from .forms import UsuarioForm
#from django.contrib.auth.forms import UsuarioForm
from django.contrib import messages
from django.core.paginator import Paginator
from .forms import UserRegisterForm

# Create your views here.
def home(request):
    mercancia = Mercancia.objects.all()
    datos = {
        'mercancia':mercancia
    }
    return render(request, 'xartgord/index.html', datos)

def personajes(request):
    return render(request, 'xartgord/personajes.html')

def items(request):
    return render(request, 'xartgord/items.html')

def enemigos(request):
    return render(request, 'xartgord/enemigos.html')

def contact(request):
    return render(request, 'xartgord/contact.html')

def mercancia(request):
    return render(request, 'xartgord/mercancia.html')

def armas(request):
    return render(request, 'xartgord/armas.html')

def armaduras(request):
    return render(request, 'xartgord/armaduras.html')

def objetos(request):
    return render(request, 'xartgord/objetos.html')

def cuenta(request):
    return render(request, 'xartgord/cuenta.html')

def polerones(request):
    return render(request, 'xartgord/polerones.html')

def usuario(request):
    return render(request, 'xartgord/usuario.html')

def registro(request):
    return render(request, 'xartgord/registro.html')

def form_mod_usuario(request):
    return render(request, 'xartgord/form_mod_usuario.html')
def listausuarios(request):
    return render(request, 'xartgord/listausuarios.html')

def login2(request):
    return render(request, 'xartgord/login2.html')

def cuentas(request):
    return render(request, 'xartgord/cuentas.html')
def form_usuario(request):
    return render(request, 'xartgord/form_usuario.html')
def listas(request):
    return render(request, 'xartgord/listas.html')
####################

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			messages.success(request, f'Usuario {username} creado')
			return redirect('home')
	else:
		form = UserRegisterForm()

	context = { 'form' : form }
	return render(request, 'xartgord/register.html', context)

#####################
def form_mercancia(request):
    mercancia = Mercancia.objects.all()
    datos = {
        'mercancia':mercancia,
        'form':MercanciaForm()
    }
    if (request.method == 'POST'):
        formulario=MercanciaForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Datos Guardados correctamente'
        else:
            formulario=MercanciaForm()
            datos['mensaje'] = 'ERROR: no se puedo guardar el producto, intentelo mas tarde'
    return render(request, 'xartgord/form_mercancia.html',datos) 

def form_modifimerca(request, id):
    mercancia = Mercancia.objects.get(idproducto=id)
    datos = {
        'form':MercanciaForm(instance=mercancia)
    }
    if(request.method == 'POST'):
        formulario = MercanciaForm(request.POST, request.FILES, instance=mercancia)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Modificado correctamente'
        else:
            formulario=MercanciaForm()
            datos['mensaje'] = 'ERROR: no se puedo guardar el producto, intentelo mas tarde'
    return render(request, 'xartgord/form_modifimerca.html',datos)  

##eliminar
def form_eliminar(request, id):
    mercancia = Mercancia.objects.get(idproducto=id)
    mercancia.delete()
    
    return redirect(to='form_mercancia')
#agregar polerones




#REGISTRAR USUARIO
def form_reg_usuario(request):
    datos = {
        'form':UsuarioForm()
    }
    if(request.method == 'POST'): #post guardar datos
        formulario = UsuarioForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Registrado correctamente'
        else:
            formulario = UsuarioForm()
            datos['mensaje'] = 'ERROR: No se ha registrado, intente nuevamente'
    return render(request,'xartgord/usuario.html',datos)

#post registrar datos usuario
def registro(request):
    datos = {
        'form':UsuarioForm()
    }
    if(request.method == 'POST'):
        formulario = UsuarioForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Registrado correctamente'
            messages.success(request, 'Registrado correctamente')
            return redirect('http://127.0.0.1:8000/form_mercancia/')
        else:
            formulario = UsuarioForm()
            datos['mensaje'] = 'ERROR: No se ha registrado, intente nuevamente'
    return render(request,'xartgord/registro.html',datos)

#MODIFICAR USUARIO
def form_mod_usuario(request,id):
    usuario = Usuario.objects.get(Rut = id)
    datos = {
        'form':UsuarioForm(instance=usuario)
    }
    
    if(request.method == 'POST'): #post guardar datos?
        formulario = UsuarioForm(request.POST, instance=usuario)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Usuario Modificado correctamente'
            return redirect(to= "usuarios")
        else:
            formulario = UsuarioForm()
            datos['mensaje'] = 'ERROR: No se ha modificado, intente nuevamente'
    return render(request,'xartgord/form_mod_usuario.html',datos)      

#ELIMINAR USUARIO
def form_mod_eliminar_usuario(request, id):
    usuario = Usuario.objects.get(Rut = id)
    usuario.delete()
    return redirect(to="usuarios")

##listar productos


def lista_mer(request, id):
    mercancia_page = Paginator.objects.all()
    mercancia = mercancia_page.get_page(1)

    return render(request,'xartgord/form_mercancia.html', {'mercancia':mercancia})   





def loginUsu(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    print(username)
    print(password)
    return render(request, 'registration/loginn.html')