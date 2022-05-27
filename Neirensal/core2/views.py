from re import template
from django.shortcuts import redirect, render, HttpResponse
from core2.Carrito import Carrito
from core2.models import Producto
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from twilio.rest import Client
from Neirensal.settings import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN
from .forms import ProductoForm

def home (request):
    #return render(request, 'core2/home.html') 
    productos= Producto.objects.all()
    datos = {
        'productos': productos
    }
    return render(request, 'core2/home.html', datos)

def stock (request):
    productos= Producto.objects.all()
    datos = {
        'productos': productos
    }
    return render(request, 'core2/stock.html', datos)

def correo (request):
    return render(request, 'core2/correo.html')

def prescripcion (request):
    return render(request, 'core2/prescripcion.html')
    

def tienda(request):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    if request.method == 'POST' :
        numero_usuario = request.POST.get('user_number')
        correo_usuario = request.POST.get('mail')
        input1 = len(numero_usuario)

        if input1 != 0: 
            user_whatsapp_number = request.POST['user_number']
            message = client.messages.create(
                from_='whatsapp:+14155238886',
                body='Enviado desde pc a usted',
                to='whatsapp:+{}'.format(user_whatsapp_number)
            )

            print(user_whatsapp_number)
            print(message.sid)

            return redirect("tienda")
        

        input2 = len(correo_usuario)
        if input2 != 0: 
            mail = request.POST.get('mail')
            
            send_email(mail)    

    productos = Producto.objects.all()
    return render(request, "core2/tienda.html", {'productos':productos})


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

def send_email(mail):
    context = {'mail': mail}
    template = get_template('core2/correo.html')
    content = template.render(context)

    email = EmailMultiAlternatives(
        'Aviso de reserva de medicamentos.',
        'nada que hacer',
        settings.EMAIL_HOST_USER,
        [mail]
    )
    email.attach_alternative(content,'text/html')
    email.send()





def form_producto(request):
    datos = {
        'form': ProductoForm()
    }
    if request.method== 'POST':
        formulario = ProductoForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Guardados correctamente"
    return render(request, 'core2/form_producto.html',datos)

def form_mod_producto(request, id):
    producto = Producto.objects.get(id=id)
    datos = {
        'form': ProductoForm(instance=producto)
    }

    if request.method== 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Modificados correctamente"
    return render(request, 'core2/form_mod_producto.html', datos)

def form_del_producto(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()
    return redirect(to="home")
