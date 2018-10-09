from django.shortcuts import render
from django.http import HttpResponse

# Creación de Vistas

def index(request):
    return HttpResponse("Hola, te encuentras en la aplicación de SOPSI.")