from datetime import datetime
from decimal import Decimal

import django_filters.rest_framework
from django.contrib.auth.models import User
from django.db import transaction
from django.shortcuts import get_object_or_404
from django.utils import timezone
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import generics, viewsets, status, mixins, serializers
from rest_framework import permissions

from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db.models import F

from patines.models import Patinete, Alquiler
from patines.serializer import PatineteSerializer, AlquilerSerializer, UsuarioSerializer


# Create your views here.
# PATINETES #
class PatineteViewSet(viewsets.ModelViewSet):
    queryset = Patinete.objects.all()
    serializer_class = PatineteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @extend_schema(
        parameters=[
            OpenApiParameter(name='estado-alquilado', description='Filtro por estado de alquiler', required=False)
        ]
    )
    # Filtrar por estado de alquiler
    @action(detail=False, methods=['GET'])
    def patinetes_alquilados(self, request):
        patinetes = Patinete.objects.filter(estado_alquiler=True)
        serializer = PatineteSerializer(patinetes, many=True, context={'request': request})
        return Response(serializer.data)

    @extend_schema(
        parameters=[
            OpenApiParameter(name='estado-libre', description='Filtro por estado de alquiler', required=False)
        ]
    )
    @action(detail=False, methods=['GET'])
    def patinetes_libres(self, request):
        patinetes = Patinete.objects.filter(estado_alquiler=False)
        serializer = PatineteSerializer(patinetes, many=True, context={'request': request})
        return Response(serializer.data)


# ALQUILAR #
class AlquilerViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin):
    serializer_class = AlquilerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Filtra los alquileres por el usuario actual
        return Alquiler.objects.filter(usuario=self.request.user)

    # Método para crear un nuevo alquiler con un patinete libre
    def perform_create(self, serializer):
        num_patinete = self.request.data.get('patinete')
        patinete = get_object_or_404(Patinete, numero=num_patinete)

        if patinete.estado_alquiler:
            raise ValidationError({'Error': 'El patinete no está libre.'})

        with transaction.atomic():
            # Guardar el alquiler
            fecha_desbloqueo = timezone.now()
            serializer.save(patinete=patinete, usuario=self.request.user, fecha_desbloqueo=fecha_desbloqueo)

            # Cambiar el estado del patinete a alquilado
            patinete.estado_alquiler = True
            patinete.save()

    # Método para liberar un alquiler y un patinete
    def liberar_patinete(self, request, *args, **kwargs):
        # Obtener el id del patinete a liberar del cuerpo de la solicitud
        num_patinete = request.data.get('patinete')
        patinete = get_object_or_404(Patinete, numero=num_patinete)

        if not patinete.estado_alquiler:
            raise ValidationError({'Error': 'El patinete no está alquilado.'})

        with transaction.atomic():
            if patinete.estado_alquiler:
                print(type(patinete))
                alquiler = get_object_or_404(Alquiler, patinete=patinete, usuario=request.user,
                                             fecha_entrega__isnull=True)
                # Obtener el alquiler del patinete

                # Calcular el coste final
                tiempo_alquilado = timezone.now() - alquiler.fecha_desbloqueo
                tiempo_total_minutos = Decimal(str(tiempo_alquilado.total_seconds())) / Decimal('60')
                coste_final = tiempo_total_minutos * Decimal(
                    str(alquiler.patinete.precio_minuto)) + patinete.precio_desbloqueo
                alquiler.coste_final = coste_final

                # Aumentar el débito del usuario
                request.user.debito = F('debito') + coste_final
                request.user.save()

                # Cambiar el estado del patinete a disponible
                alquiler.patinete.estado_alquiler = False
                alquiler.patinete.save()

                # Actualizar la fecha de entrega del alquiler
                fecha_entrega = timezone.now()
                alquiler.fecha_entrega = fecha_entrega
                alquiler.save()
                print('se ha liberado la patineta')
                return Response({'message': 'El patinete ha sido liberado.'}, status=status.HTTP_200_OK)


class ListadoAlquilerViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    Clase para listar todos los alquileres de los usuarios
    """
    queryset = Alquiler.objects.all()
    serializer_class = AlquilerSerializer
    permission_classes = [permissions.IsAdminUser]




class UsuariosViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    Clase para listar todos los patines libres
    """
    queryset = User.objects.all().order_by('-debito')
    serializer_class = UsuarioSerializer
    permission_classes = [permissions.IsAdminUser]
