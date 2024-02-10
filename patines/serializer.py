from django.contrib.auth.models import User
from rest_framework import serializers

from patines.models import *


class PatineteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patinete
        fields = ['numero', 'tipo', 'precio_desbloqueo', 'precio_minuto', 'estado_alquiler', 'url']


class AlquilerSerializer(serializers.HyperlinkedModelSerializer):
    patinete = serializers.PrimaryKeyRelatedField(queryset=Patinete.objects.all())
    usuario = serializers.SerializerMethodField()

    class Meta:
        model = Alquiler
        fields = ['patinete', 'usuario', 'fecha_desbloqueo', 'fecha_entrega', 'coste_final', 'url']

    def get_usuario(self, obj):
        """
        Devuelve el nombre de usuario en lugar del id
        """
        return obj.usuario.username


class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    debito = serializers.DecimalField(max_digits=10, decimal_places=2)
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'debito']
