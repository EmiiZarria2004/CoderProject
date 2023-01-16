from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Modelo, Motor, Proyecto
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from AppCoder.forms import *
from django.contrib.auth.decorators import login_required

# Create your views here.





#Pagina principal
def inicio(request):
	return  render(request, "AppCoder/inicio.html")





#Botones en barra de navegacion
def sobremi(request):
	return render(request, "AppCoder/sobremi.html")

def jdm(request):
	return render(request, "AppCoder/jdm.html")

def crudcompleto(request):
	return render(request, "AppCoder/crudcompleto.html")





#agregar modelos
@login_required
def modeloForm(request):

	if request.method == "POST":
		modelo = Modelo(nmb_marca=request.POST["marca"], nmb_mod=request.POST["nombre"], id_mod=request.POST["id"], car_esp=request.POST["caresp"], imagenfront=request.FILES["imagenfront"], imagenback=request.FILES["imagenback"], fecha_prod=request.POST["produccion"], default_motor=request.POST["motor"], transm=request.POST["trans"], precio_prom=request.POST["preciopromedio"])
		modelo.save()
	return render(request, "AppCoder/modeloForm.html")





#agregar motores
@login_required
def motorForm(request):
	if request.method == "POST":
		motor = Motor(nmb_motor=request.POST["nombre"], imagen=request.FILES["imagen"], hp_default=request.POST["hpdefault"], cil=request.POST["cilindrada"], hp_max=request.POST["hpmax"], precio_prom=request.POST["preciopromedio"])
		motor.save()
	return render(request, "AppCoder/motorForm.html")





#agregar actividades
@login_required
def actividadForm(request):
	if request.method == "POST":
		actividad = Proyecto(actividad=request.POST["nombre"], descripcion=request.POST["descripcion"])
		actividad.save()
	return render(request, "AppCoder/actividadForm.html")





#mostrar resultados de busqueda
def modeloResultado(request):

	if request.GET["modelo"]:
		modelo = request.GET["modelo"]
		modelos = Modelo.objects.filter(nmb_mod__icontains=modelo)

		return render(request, "AppCoder/resultadosmod.html", {"modelos":modelos, "modelo":modelo})
	
	else:
		respuesta="No enviaste ningun dato."

	return HttpResponse(respuesta)

def motorResultado(request):

	if request.GET["motor"]:
		motor = request.GET["motor"]
		motores = Motor.objects.filter(nmb_motor__icontains=motor)

		return render(request, "AppCoder/resultadosmotor.html", {"motores":motores, "motor":motor})

	else:
		respuesta="No enviaste ningun dato."

	return HttpResponse(respuesta)

def actividadResultado(request):

	if request.GET["actividad"]:
		actividad = request.GET["actividad"]
		actividades = Proyecto.objects.filter(actividad__icontains=actividad)

		return render(request, "AppCoder/resultadosact.html", {"actividades":actividades, "actividad":actividad})

	else:
		respuesta="No enviaste ningun dato."

	return HttpResponse(respuesta)





#Leer
def mostrarModelos(request):
	vermodelos = Modelo.objects.all()
	contexto = {"vermodelos": vermodelos}
	return render(request, "AppCoder/modelos.html", contexto)

def mostrarMotores(request):
	vermotores = Motor.objects.all()
	contexto = {"vermotores": vermotores}
	return render(request, "AppCoder/motores.html", contexto)

def mostrarActividades(request):
	veractividades = Proyecto.objects.all()
	contexto = {"veractividades": veractividades}
	return render(request, "AppCoder/proyectos.html", contexto)





#Iniciar sesion
def InicioSesion(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data = request.POST)

		if form.is_valid():
			usuario = form.cleaned_data.get("username")
			contra = form.cleaned_data.get("password")

			user = authenticate(username = usuario, password = contra)

			if user:
				login(request, user)
				return render(request, "AppCoder/inicio.html", {"mensaje":f"{user}"})

		else:
			return render(request, "AppCoder/loginerror.html", {"mensaje":"Los datos que ingresaste no estan registrados"})

	else:
		form = AuthenticationForm()

	return render(request, "AppCoder/login.html", {"loginform":form})





#Para continuar debes iniciar sesion

def RequestLogin(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data = request.POST)

		if form.is_valid():
			usuario = form.cleaned_data.get("username")
			contra = form.cleaned_data.get("password")

			user = authenticate(username = usuario, password = contra)

			if user:
				login(request, user)
				return render(request, "AppCoder/inicio.html", {"mensaje":f"{user}"})

		else:
			return render(request, "AppCoder/loginerror.html", {"mensaje":"Los datos que ingresaste no estan registrados"})

	else:
		form = AuthenticationForm()

	return render(request, "AppCoder/requestlogin.html", {"loginform":form})





#Registrar un usuario
def RegistroUsuario(request):
	if request.method == "POST":
		form = UsuarioRegistro(request.POST)

		if form.is_valid():
			username = form.cleaned_data["username"]
			form.save()
			return render(request, "AppCoder/registro.html", {"mensaje2":f'Se agrego el usuario "{username}" correctamente.'})

	else:
		form = UsuarioRegistro()
	return render(request, "AppCoder/registro.html", {"registroform":form})





#Agregar un avatar
@login_required
def AgregarAvatar(request):

	if request.method == "POST":
		form = AvatarFormulario(request.POST, request.FILES)

		if form.is_valid():
			usuarioActual = User.objects.get(username=request.user)
			avatar = Avatar(usuario=usuarioActual, imagen=form.cleaned_data["imagen"])
			avatar.save()

			return render(request, "AppCoder/inicio.html")

	else:
		form = AvatarFormulario()

	return render(request, "AppCoder/agregarAvatar.html", {"formulario":form})





#Editar un usuario
@login_required
def EditarUsuario(request):
	usuario = request.user

	if request.method == "POST":
		form = EditarForm(request.POST)

		if form.is_valid():

			info = form.cleaned_data

			usuario.email = info["email"]
			usuario.set_password(info["password1"])
			usuario.first_name = info["nombre"]
			usuario.last_name = info["apellido"]

			usuario.save()
			return render(request, "AppCoder/inicio.html")

	else:
		form = EditarForm(initial={
			"email":usuario.email,
			"nombre":usuario.first_name,
			"apellido":usuario.last_name,
		})
	return render(request, "AppCoder/editaruser.html", {"editarform":form, "usuario":usuario})





#Leer y eliminar en "Crud Completo"
@login_required
def mostrarModelos2(request):
	vermodelos = Modelo.objects.all()
	contexto = {"vermodelos": vermodelos}
	return render(request, "AppCoder/eliminarmod.html", contexto)

@login_required
def EliminarMod(request, modeloNombre):
	modelo = Modelo.objects.get(nmb_mod=modeloNombre)
	modelo.delete()

	modelos = Modelo.objects.all()
	contexto = {"models":modelos}

	return render(request, "AppCoder/crudcompleto.html", contexto)

@login_required
def mostrarMotores2(request):
	vermotores = Motor.objects.all()
	contexto = {"vermotores": vermotores}
	return render(request, "AppCoder/eliminarmotor.html", contexto)

@login_required
def EliminarMotor(request, motorNombre):
	motor = Motor.objects.get(nmb_motor=motorNombre)
	motor.delete()

	motores = Motor.objects.all()
	contexto = {"motors":motores}

	return render(request, "AppCoder/crudcompleto.html", contexto)

@login_required
def mostrarActividades2(request):
	veractividades = Proyecto.objects.all()
	contexto = {"veractividades": veractividades}
	return render(request, "AppCoder/eliminaractividad.html", contexto)

@login_required
def EliminarAct(request, actividadNombre):
	actividad = Proyecto.objects.get(actividad=actividadNombre)
	actividad.delete()

	actividades = Proyecto.objects.all()
	contexto = {"proyectos":actividades}

	return render(request, "AppCoder/crudcompleto.html", contexto)





#Editar modelos
@login_required
def EditarMod(request, modeloNombre):
	modelo = Modelo.objects.get(car_esp=modeloNombre)

	if request.method == "POST":
		miFormulario = ModeloFormulario(request.POST, request.FILES)

		if miFormulario.is_valid():
			info = miFormulario.cleaned_data

			modelo.nmb_marca = info["nmb_marca"]
			modelo.nmb_mod = info["nmb_mod"]
			modelo.id_mod = info["id_mod"]
			modelo.car_esp = info["car_esp"]
			modelo.fecha_prod = info["fecha_prod"]
			modelo.imagenfront = info["imagenfront"]
			modelo.imagenback = info["imagenback"]
			modelo.default_motor = info["default_motor"]
			modelo.transm = info["transm"]
			modelo.precio_prom = info["precio_prom"]
			modelo.save()
			return render(request, "AppCoder/crudcompleto.html")

	else:
		miFormulario = ModeloFormulario(initial={"nmb_marca":modelo.nmb_marca, "nmb_mod":modelo.nmb_mod, "id_mod":modelo.id_mod, "car_esp":modelo.car_esp,
		"fecha_prod":modelo.fecha_prod,"imagenfront":modelo.imagenfront,"imagenback":modelo.imagenback, "default_motor":modelo.default_motor, "transm":modelo.transm, "precio_prom":modelo.precio_prom})
	return render(request, "AppCoder/editarMod.html", {"miFormulario":miFormulario, "car_esp":modeloNombre})





#Editar motores
@login_required
def EditarMotor(request, motorNombre):
	motor = Motor.objects.get(nmb_motor=motorNombre)

	if request.method == "POST":
		miFormulario = MotorFormulario(request.POST, request.FILES)

		if miFormulario.is_valid():
			info = miFormulario.cleaned_data

			motor.nmb_motor = info["nmb_motor"]
			motor.imagen = info["imagen"]
			motor.hp_default = info["hp_default"]
			motor.cil = info["cil"]
			motor.hp_max = info["hp_max"]
			motor.precio_prom = info["precio_prom"]
			motor.save()
			return render(request, "AppCoder/crudcompleto.html")

	else:
		miFormulario = MotorFormulario(initial={"nmb_motor":motor.nmb_motor,"imagen":motor.imagen, "hp_default":motor.hp_default, "cil":motor.cil, "hp_max":motor.hp_max,
		"precio_prom":motor.precio_prom})
	return render(request, "AppCoder/editarMotor.html", {"miFormulario":miFormulario, "nmb_motor":motorNombre})





#Editar actividades
@login_required
def EditarAct(request, actividadNombre):
	actividad = Proyecto.objects.get(actividad=actividadNombre)

	if request.method == "POST":
		miFormulario = ActividadFormulario(request.POST)

		if miFormulario.is_valid():
			info = miFormulario.cleaned_data

			actividad.actividad = info["actividad"]
			actividad.descripcion = info["descripcion"]
			actividad.save()
			return render(request, "AppCoder/crudcompleto.html")

	else:
		miFormulario = ActividadFormulario(initial={"actividad":actividad.actividad, "descripcion":actividad.descripcion})
	return render(request, "AppCoder/editarAct.html", {"miFormulario":miFormulario, "actividad":actividadNombre})





#Terminos de uso y politicas de privacidad
def TerminosDeUso(request):
	return render(request, "AppCoder/terms.html")


