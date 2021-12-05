from django.http import HttpResponse
from datetime import datetime

def saludo(request):
    return HttpResponse("Soy Gustavo y hago un saludo de Hola mundo")

def segundaVista(request):
    return HttpResponse("Soy Gustavo y hago una segunda vista a Hola mundo")

def dia(request):
    variable = datetime.now()
    return HttpResponse(f"Hoy es un gran dia {variable}")

def apellido(request, ape):
    return HttpResponse(f"Mi apellido es {ape}, Es muy bueno")