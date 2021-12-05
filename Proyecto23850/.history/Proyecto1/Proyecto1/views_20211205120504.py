from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Soy Gustavo y hago un saludo de Hola mundo")

