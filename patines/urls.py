from django.urls import path, include
from rest_framework.routers import DefaultRouter
from patines import views

router = DefaultRouter()
router.register(r'patinetes', views.PatineteViewSet, basename='patinete')

urlpatterns = [
    path('', include(router.urls)),
]