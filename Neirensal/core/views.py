from re import template
from django.shortcuts import redirect, render, HttpResponse
from core.Carrito import Carrito
from core.models import Producto
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from twilio.rest import Client
from Neirensal.settings import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN
from .forms import ProductoForm

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

def correo (request):
    return render(request, 'core/correo.html')

def prescripcion (request):
    return render(request, 'core/prescripcion.html')
    

def tienda(request):
    if request.method == 'POST':
        mail = request.POST.get('mail')
        send_email(mail)
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

def send_email(mail):
    context = {'mail': mail}
    template = get_template('core/correo.html')
    content = template.render(context)

    email = EmailMultiAlternatives(
        'Aviso de reserva de medicamentos.',
        'nada que hacer',
        settings.EMAIL_HOST_USER,
        [mail]
    )
    email.attach_alternative(content,'text/html')
    email.send()

#order_details = {
    #'amount': '5kg',
    #'item': 'Tomatoes',
    #'date_of_delivery': '03/04/2021',
    #'address': 'No 1, Ciroma Chukwuma Adekunle Street, Ikeja, Lagos'
#}

def send_notification(request):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    if request.method == 'POST':
        user_whatsapp_number = request.POST['num_usuario']

        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body='Mensaje enviado de Mon, avisame si llego xd',
            to='whatsapp:+{}'.format(user_whatsapp_number)
        )

        print(user_whatsapp_number)
        print(message.sid)
        return HttpResponse('Great! Expect a message...')

    return render(request, 'phone.html')

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
            datos['mensaje'] = "Modificados correctamente"
    return render(request, 'core/form_mod_producto.html', datos)

def form_del_producto(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()
    return redirect(to="home")
