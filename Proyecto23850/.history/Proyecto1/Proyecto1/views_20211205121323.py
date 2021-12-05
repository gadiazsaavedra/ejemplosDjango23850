from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Soy Gustavo y hago un saludo de Hola mundo")

def segundaVista(request):
    return HttpResponse("Soy Gustavo y hago una segunda vista a Hola mundo")

def dia(request):
    variable = datetime.datetime.now