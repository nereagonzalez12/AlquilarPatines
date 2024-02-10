from django.urls import path, include
from rest_framework.routers import DefaultRouter
from patines import views

router = DefaultRouter()
router.register(r'patinetes', views.PatineteViewSet, basename='patinete')
router.register(r'alquiler', views.AlquilerViewSet, basename='alquiler')
router.register(r'alquileres', views.ListadoAlquilerViewSet, basename='alquileres')
router.register(r'usuarios', views.UsuariosViewSet, basename='usuarios')

urlpatterns = [
    path('', include(router.urls)),
    path('liberar-patinete/', views.AlquilerViewSet.as_view({'post': 'liberar_patinete'}), name='liberar_patinete'),

]