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
from core.views import correo, registrado, agregarP, eliminarP, limpiarC, restarP, register, tienda,home,send_notification,stock,prescripcion
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
    path('prescripcion',prescripcion, name="prescripcion"), 
    path('agregar/<int:id_remedio>/', agregarP, name="Agg"),
    path('eliminar/<int:producto_id>/', eliminarP, name="Ell"),
    path('restar/<int:producto_id>/', restarP, name="Sub"),
    path('limpiar/', limpiarC, name="CLS"),
    path('', send_notification),
]
