
from django.urls import path
from Aplicacion.views import curso


urlpatterns = [
    path("curso/", curso, name="curso")
    
]
