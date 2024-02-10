from django.contrib.auth.models import User
from rest_framework import serializers

from patines.models import *


class PatineteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patinete
        fields = ['numero', 'tipo', 'precio_desbloqueo', 'precio_minuto', 'estado_alquiler', 'url']


class AlquilerSerializer(serializers.HyperlinkedModelSerializer):
    patinete = serializers.PrimaryKeyRelatedField(queryset=Patinete.objects.all())
    class Meta:
        model = Alquiler
        fields = ['patinete', 'url', 'fecha_desbloqueo', 'fecha_entrega', 'coste_final']


class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'debito']
