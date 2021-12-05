from django.http import HttpResponse
from datetime import datetime
from django


def saludo(request):
    return HttpResponse("Soy Gustavo y hago un saludo de Hola mundo")

def segundaVista(request):
    return HttpResponse("Soy Gustavo y hago una segunda vista a Hola mundo")

def dia(request):
    variable = datetime.now()
    return HttpResponse(f"Hoy es un gran dia {variable}")

def apellido(request, ape):
    fecha = datetime.now()
    return HttpResponse(f"Mi apellido es {ape}, y soy muy bueno .. <br><br>.. Por lo menos hoy: {fecha}")

def probandoTemplate(request):
    miHTML = open("C:/Users/gdiaz/OneDrive/GOOGLE DRIVE/Gustavo/Curso programacion/Coder House/Proyecto23850/Proyecto1/Proyecto1/Plantillas/template1.html")
    plantilla = Template(miHTML.read())