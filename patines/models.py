from django.conf import settings
from django.conf.global_settings import AUTH_USER_MODEL
from django.db import models


# Create your models here.

#
# Modelo Patinete
class Patinete(models.Model):
    numero = models.PositiveIntegerField(unique=True)
    tipo = models.CharField(max_length=50)
    precio_desbloqueo = models.DecimalField(max_digits=12, decimal_places=2)
    precio_minuto = models.DecimalField(max_digits=12, decimal_places=2)
    estado_alquiler = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.tipo} - {self.numero}"


class Alquiler(models.Model):
    patine = models.ForeignKey(Patinete, on_delete=models.CASCADE)
    estado = models.CharField(max_length=50)
    usuario = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    fecha_desbloqueo = models.DateField()
    fecha_entrega = models.DateField()
    coste_final = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.patine} {self.estado} [ alquilado por {self.usuario} ]"


# Clase usuario con campo adicional
class Usuario(models.Model):
    usuario = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    debito = models.DecimalField(max_digits=12, decimal_places=2, default=0)
