
from django.urls import path
from Aplicacion.views import *

urlpatterns = [
    path("", inicio),
    path("cursos/",cursos),
    path("profesores/", profesores, name="profe"),
    path("estudiantes/", estudiantes, name="estudiantes"),
    path("entregables/",entregables, name="entregables"),
    path("curso/",curso,name="curso" ),   
]
