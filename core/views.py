from re import template
from django.shortcuts import redirect, render, HttpResponse
from core.Carrito import Carrito
from core.models import Producto, Remedio
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from twilio.rest import Client
from Neirensal.settings import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN

def home (request):
    #return render(request, 'core/home.html') 
    remedios= Remedio.objects.all()
    datos = {
        'remedios': remedios
    }
    return render(request, 'core/home.html', datos)

def correo (request):
    return render(request, 'core/correo.html')

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
    return redirect("Tienda")

def eliminarP(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("Tienda")

def restarP(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("Tienda")

def limpiarC(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("Tienda")

def send_email(mail):
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
        return HttpResponse('Great! Expect a message...')

    return render(request, 'phone.html')