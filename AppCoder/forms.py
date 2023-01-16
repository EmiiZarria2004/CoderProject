from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from AppCoder.models import *

class ModeloFormulario(forms.Form):

	nmb_marca = forms.CharField()
	nmb_mod = forms.CharField()
	id_mod = forms.CharField()
	car_esp = forms.CharField()
	imagenfront = forms.ImageField()
	imagenback = forms.ImageField()
	fecha_prod = forms.CharField()
	default_motor = forms.CharField()
	transm = forms.CharField()
	precio_prom = forms.CharField()

class MotorFormulario(forms.Form):
	nmb_motor = forms.CharField()
	imagen = forms.ImageField()
	hp_default = forms.IntegerField()
	cil = forms.CharField()
	hp_max = forms.IntegerField()
	precio_prom = forms.CharField()

class ActividadFormulario(forms.Form):
	actividad = forms.CharField()
	descripcion = forms.CharField()

class UsuarioRegistro(UserCreationForm):

	email = forms.EmailField()
	password1 = forms.CharField(label = "Password", widget=forms.PasswordInput)
	password2 = forms.CharField(label = "Vuelve a escribir la password", widget=forms.PasswordInput)

	class Meta:

		model = User
		fields = ["username", "email", "first_name", "last_name", "password1", "password2"]

class EditarForm(UserCreationForm):

	email = forms.EmailField()
	nombre = forms.CharField()
	apellido = forms.CharField()
	password1 = forms.CharField(label = "Password", widget=forms.PasswordInput)
	password2 = forms.CharField(label = "Vuelve a escribir la password", widget=forms.PasswordInput)

	class Meta:

		model = User
		fields = [ 'email', 'password1', 'password2']

class AvatarFormulario(forms.ModelForm):
	class Meta:
		model = Avatar
		fields = ["imagen"]
	
