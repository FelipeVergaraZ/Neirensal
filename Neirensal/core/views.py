from django.shortcuts import redirect, render, HttpResponse
from core.Carrito import Carrito
from core.models import Producto
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

# Create your views here.

def home (request):
    return render(request, 'core/home.html')

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
