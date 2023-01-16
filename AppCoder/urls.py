from django.urls import path
from AppCoder.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", inicio, name="Inicio"),
    path('sobremi/', sobremi, name="Sobre mi"),
    path('jdm/', jdm, name="JDM"),
    path('modelos/resultado/', modeloResultado, name="resultado"),
    path('motores/resultado/', motorResultado, name="resultado2"),
    path('actividades/resultado/', actividadResultado, name="resultado3"),
    path('login/', InicioSesion, name="Login"),
    path('register/', RegistroUsuario, name="Register"),
    path('logout/', LogoutView.as_view(template_name="AppCoder/logout.html"), name="Logout"),
    path('requestlogin/', RequestLogin, name="RequestLog"),
    path('editaruser/', EditarUsuario, name="EditUser"),
    path('agregarAvatar/', AgregarAvatar, name="Avatar"),
    path('terminosdeuso/', TerminosDeUso, name="Terms"),
    
    #CrudCompleto
    path('crudcompleto/', crudcompleto, name="CrudCompleto"),
    path('modelos/', mostrarModelos, name="Modelos"),
    path('motores/', mostrarMotores, name="Motores"),
    path('actividades/', mostrarActividades, name="Actividades"),
    path('modelosform/', modeloForm, name="FormularioMod"),
    path('motoresform/', motorForm, name="FormularioMotores"),
    path('actividadesform/', actividadForm, name="FormularioAct"),
    path('mostrarMod/', mostrarModelos2, name="BorrarMod"),
    path('eliminarModelo/<modeloNombre>', EliminarMod, name="EliminarModelo"),
    path('mostrarMotor/', mostrarMotores2, name="BorrarMotor"),
    path('eliminarMotor/<motorNombre>', EliminarMotor, name="EliminarMotor"),
    path('mostrarActividad/', mostrarActividades2, name="BorrarActividad"),
    path('eliminarActividad/<actividadNombre>', EliminarAct, name="EliminarAct"),
    path('editarMod/<modeloNombre>', EditarMod, name="EditarMod"),
    path('editarMotor/<motorNombre>', EditarMotor, name="EditarMotor"),
    path('editarAct/<actividadNombre>', EditarAct, name="EditarAct"),
]