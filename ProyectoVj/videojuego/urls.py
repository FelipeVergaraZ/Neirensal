from django.urls import path
from .views import cuentas, form_reg_usuario, form_usuario, home, items, listausuarios, polerones, register, registro, usuario,login2
from .views import personajes, contact
from .views import enemigos, mercancia
from .views import armaduras, armas, home
from .views import personajes, contact, items
from .views import enemigos, mercancia, objetos,cuenta
from .views import form_mercancia, form_modifimerca,form_eliminar
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('',home,name='home'),
    path('personajes/',personajes,name='personajes'),
    path('enemigos/',enemigos,name='enemigos'),
    path('contact/',contact,name='contact'),
    path('armaduras/',armaduras,name='armaduras'),
    path('objetos/',objetos,name='objetos'),
    path('armas/',armas,name='armas'),
    path('mercancia/',mercancia,name='mercancia'),
    path('items/',items,name='items'),
    path('cuenta/',cuenta,name='cuenta'),
    path('polerones/',polerones,name='polerones'),
    
    path('usuario/',usuario,name='usuario'),

    path('loginn/', LoginView.as_view(template_name='xartgord/loginn.html'), name='loginn'),
    path('logout/', LogoutView.as_view(template_name='xartgord/logout.html'), name='logout'),
    path('registro/',registro,name='registro'),
    path('login2/',login2,name='login2'),
    path('register/',views.register,name='register'),


    path('form_mod_usuario/',form_reg_usuario,name='form_mod_usuario'),
    path('form_usuario/',form_usuario,name='from_usuario'),
    path('form_mercancia/',form_mercancia,name='form_mercancia'),
    path('cuentas/',cuentas,name='cuentas'),
    path('listausuarios/',listausuarios,name='listausuarios'),
    path('form_modifimerca/<id>/',form_modifimerca,name='form_modifimerca'),
    path('form_eliminar/<id>/',form_eliminar,name='form_eliminar'),
    



]



