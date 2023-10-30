from django.shortcuts import render
from django.http import HttpResponse
from Aplicacion.models import Curso


# Create your views here.
def curso(self):
    curso=Curso(nombre="PythonFlex", comision=56050)
    curso.save()
    documentoDeTexto= f"------>Curso {curso.nombre} comisión {curso.comision}"
    return HttpResponse(documentoDeTexto)

def inicio(request):
    return render(request, "AppCoder/index.html")
def cursos(request):
    return HttpResponse("Vista Cursos")
def profesores(request):
    return HttpResponse("Vista Profesores")
def estudiantes(request):
    return render(request, "Appcoder/estudiantes.html")
def entregables(request):
    return HttpResponse("Vista Entregables")