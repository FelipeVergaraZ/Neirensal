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
from django.urls import path
from core.views import correo,agregarP, eliminarP, limpiarC, restarP, tienda,home,send_notification

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home ,name="home"),
    path('tienda',tienda , name="tienda"),
    path('correo',correo, name="correo"),  
    path('agregar/<int:producto_id>/', agregarP, name="Agg"),
    path('eliminar/<int:producto_id>/', eliminarP, name="Ell"),
    path('restar/<int:producto_id>/', restarP, name="Sub"),
    path('limpiar/', limpiarC, name="CLS"),
    path('', send_notification),
]
