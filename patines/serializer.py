from django.contrib.auth.models import User
from rest_framework import serializers

from patines.models import *


class PatineteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patinete
        fields = ['numero', 'tipo', 'precio_desbloqueo', 'precio_minuto', 'url']


