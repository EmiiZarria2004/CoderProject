from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Modelo(models.Model):

	def __str__(self):
		return f"{self.nmb_marca} {self.nmb_mod} {self.id_mod} {self.car_esp} {self.fecha_prod}" 

	nmb_marca = models.CharField(max_length=20)
	nmb_mod = models.CharField(max_length=30)
	id_mod = models.CharField(max_length=20)
	car_esp = models.CharField(max_length=20)
	fecha_prod = models.CharField(max_length=9)
	imagenfront = models.ImageField(upload_to="modelos", null=True, blank=True)
	imagenback = models.ImageField(upload_to="modelos", null=True, blank=True)
	default_motor = models.CharField(max_length=20)
	transm = models.CharField(max_length=20)
	precio_prom = models.CharField(max_length=20)

class Motor(models.Model):

	def __str__(self):
		return f"{self.nmb_motor} {self.cil}"

	nmb_motor = models.CharField(max_length=20)
	imagen = models.ImageField(upload_to="motores", null=True, blank=True)
	hp_default = models.IntegerField()
	cil = models.CharField(max_length=20)
	hp_max = models.IntegerField()
	precio_prom = models.CharField(max_length=20)

class Proyecto(models.Model):

	def __str__(self):
		return f"{self.actividad}"

	actividad = models.CharField(max_length=20)
	descripcion = models.CharField(max_length=300, default="Falta descripción.")

class Avatar(models.Model):
	usuario = models.ForeignKey(User, on_delete=models.CASCADE)
	imagen = models.ImageField(upload_to="avatares", null=True, blank=True)


