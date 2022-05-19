"""Neirensal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core.views import correo, registrado, agregarP, eliminarP, limpiarC, restarP, register, tienda,home,send_notification,stock,pacientes,reserva,form_producto,form_mod_producto,form_del_producto,form_paciente,form_mod_paciente,form_del_paciente,form_reserva,form_mod_reserva,form_del_reserva
from django.contrib.auth.views import LoginView, LogoutView
from core import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',home ,name="home"),
    path('stock',stock , name="stock"),
    path('tienda',tienda , name="tienda"),
    path('registrado/', registrado , name="registrado"),
    path('register/',views.register,name='register'),
    path('logout/', LogoutView.as_view(template_name='core/logout.html'), name='logout'),
    path('', LoginView.as_view(template_name='core/loginn.html'), name='loginn'),
    path('correo',correo, name="correo"), 
    path('pacientes',pacientes, name="pacientes"),
    path('reserva',reserva, name="reserva"),  
    path('agregar/<int:id_remedio>/', agregarP, name="Agg"),
    path('eliminar/<int:producto_id>/', eliminarP, name="Ell"),
    path('restar/<int:producto_id>/', restarP, name="Sub"),
    path('limpiar/', limpiarC, name="CLS"),
    path('', send_notification),
    path('form_producto', form_producto, name="form_producto"),
    path('form_mod_producto/<id>', form_mod_producto, name="form_mod_producto"),
    path('form_del_producto/<id>', form_del_producto, name="form_del_producto"),
    path('form_paciente', form_paciente, name="form_paciente"),
    path('form_mod_paciente/<id>', form_mod_paciente, name="form_mod_paciente"),
    path('form_del_paciente/<id>', form_del_paciente, name="form_del_paciente"),
    path('form_reserva', form_reserva, name="form_reserva"),
    path('form_mod_reserva/<id>', form_mod_reserva, name="form_mod_reserva"),
    path('form_del_reserva/<id>', form_del_reserva, name="form_del_reserva"),
]
