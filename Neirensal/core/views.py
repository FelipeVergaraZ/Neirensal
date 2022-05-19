from pyexpat.errors import messages
from re import template
from django.shortcuts import redirect, render, HttpResponse
from core.Carrito import Carrito
from core.models import Paciente, Producto
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from twilio.rest import Client
from Neirensal.settings import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN
from core.forms import UserRegisterForm
from django.contrib import messages
from .forms import ProductoForm, PacienteForm

def home (request):
    #return render(request, 'core/home.html') 
    productos= Producto.objects.all()
    datos = {
        'productos': productos
    }
    return render(request, 'core/home.html', datos)

def stock (request):
    productos= Producto.objects.all()
    datos = {
        'productos': productos
    }
    return render(request, 'core/stock.html', datos)

def stockmed (request):
    productos= Producto.objects.all()
    datos = {
        'productos': productos
    }
    return render(request, 'core/stockmed.html', datos)

def correo (request):
    return render(request, 'core/correo.html')

def prescripcion (request):
    return render(request, 'core/prescripcion.html')
    
def registrado (request):
    return render(request, 'core/registrado.html')    

def tienda(request):
    
    if request.method == 'POST':
        var1 = request.POST.get('mail')
        var2 = request.POST.get('user_number')
        xd = len(var1)
        xd2 = len(var2)
        if xd != 0:
            mail = request.POST.get('mail')
            send_email(mail)
        if xd2 != 0:
            send_notification()
    productos = Producto.objects.all()
    return render(request, "core/tienda.html", {'productos':productos})


def agregarP(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect("tienda")

def eliminarP(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("tienda")

def restarP(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("tienda")

def limpiarC(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("tienda")

def send_email(request,mail):
    context = {'mail': mail}
    template = get_template('core/correo.html')
    content = template.render(context)

    email = EmailMultiAlternatives(
        'Un correo de prueba',
        'nada que hacer',
        settings.EMAIL_HOST_USER,
        [mail]
    )
    email.attach_alternative(content,'text/html')
    email.send()

    return render(request, "phone.html")

order_details = {
    'amount': '5kg',
    'item': 'Tomatoes',
    'date_of_delivery': '03/04/2021',
    'address': 'No 1, Ciroma Chukwuma Adekunle Street, Ikeja, Lagos'
}

def send_notification(request):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    if request.method == 'POST':
        user_whatsapp_number = request.POST['user_number']

        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body='Mensaje enviado de Mon, avisame si llego xd',
            to='whatsapp:+{}'.format(user_whatsapp_number)
        )

        print(user_whatsapp_number)
        print(message.sid)
        

    return render(request, 'phone.html')


def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			return render(request, 'core/registrado.html')
	else:
		form = UserRegisterForm()

	context = { 'form' : form }
	return render(request, 'core/register.html', context)

    
def loginUsu(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    print(username)
    print(password)
    return render(request, 'core/loginn.html')

def form_producto(request):
    datos = {
        'form': ProductoForm()
    }
    if request.method== 'POST':
        formulario = ProductoForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Guardados correctamente"
    return render(request, 'core/form_producto.html',datos)

def form_mod_producto(request, id):
    producto = Producto.objects.get(id=id)
    datos = {
        'form': ProductoForm(instance=producto)
    }

    if request.method== 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Modificados Correctamente"
    return render(request, 'core/form_mod_producto.html', datos)

def form_del_producto(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()
    return redirect(to="home")

def form_paciente(request):
    datos = {
        'form': PacienteForm()
    }
    if request.method== 'POST':
        formulario = PacienteForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Guardados Correctamente"
    return render(request, 'core/form_paciente.html',datos)

def form_mod_paciente(request, id):
    paciente = Paciente.objects.get(numero=id)
    datos = {
        'form': PacienteForm(instance=paciente)
    }
    if request.method== 'POST':
        formulario = PacienteForm(date=request.POST,instance=paciente)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Modificados Correctamente"
    return render(request, 'core/form_mod_paciente.html', datos)

def form_del_paciente(request, id):
    paciente = Paciente.objects.get(numero=id)
    paciente.delete()
    return redirect(to="home")

def pacientes (request):
    pacientes = Paciente.objects.all()
    datos = {
        'pacientes': pacientes
    }
    return render(request, 'core/pacientes.html', datos)

def pacientesmed (request):
    pacientes = Paciente.objects.all()
    datos = {
        'pacientes': pacientes
    }
    return render(request, 'core/pacientesmed.html', datos)