from django.conf import settings
from django.conf.global_settings import AUTH_USER_MODEL
from django.db import models
from django.utils import timezone


# Create your models here.

#
# Modelo Patinete
class Patinete(models.Model):

    numero = models.PositiveIntegerField(unique=True)
    tipo = models.CharField(max_length=50)
    precio_desbloqueo = models.DecimalField(max_digits=12, decimal_places=2)
    precio_minuto = models.DecimalField(max_digits=12, decimal_places=2)
    estado_alquiler = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.tipo} - {self.numero}"


class Alquiler(models.Model):
    patinete = models.ForeignKey(Patinete, on_delete=models.CASCADE)
    usuario = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    fecha_desbloqueo = models.DateTimeField(null=True)
    fecha_entrega = models.DateTimeField(null=True)
    coste_final = models.DecimalField(max_digits=12, decimal_places=2, null=True)

    def __str__(self):
        return f"{self.patinete} [ alquilado por {self.usuario} ]"

    class Meta:
        verbose_name_plural = "Alquileres"
        ordering = ["fecha_entrega"]


# Usuario con campo adicional
debito = models.ForeignKey('auth.User', related_name='debito', on_delete=models.CASCADE)