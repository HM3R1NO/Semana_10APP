from django.shortcuts import render
from django.http import HttpResponse
from Aplicacion.models import Curso


# Create your views here.
def curso(self):
    curso=Curso(nombre="PythonFlex", comision=56050)
    curso.save()
    documentoDeTexto= f"------>Curso {curso.nombre} comisión {curso.comision}"
    return HttpResponse(documentoDeTexto)