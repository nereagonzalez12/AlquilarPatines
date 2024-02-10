import django_filters.rest_framework
from rest_framework import generics, viewsets
from rest_framework import permissions
from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework.decorators import action
from rest_framework.response import Response

from patines.models import Patinete
from patines.serializer import PatineteSerializer


# Create your views here.
# PATINETES #
class PatineteViewSet(viewsets.ModelViewSet):
    queryset = Patinete.objects.all()
    serializer_class = PatineteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
