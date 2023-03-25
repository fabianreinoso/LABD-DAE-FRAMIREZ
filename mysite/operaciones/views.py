from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Colocar en la url ejemplo (sumar/17/29)")

def sumar(request, n1, n2):
    sumar = n1 + n2
    return HttpResponse(f"La suma de {n1} + {n2} = {sumar}")

def restar(request, n1, n2):
    restar = n1 - n2
    return HttpResponse(f"La resta de {n1} - {n2} = {restar}")

def multiplicar(request, n1, n2):
    multiplicar = n1 * n2
    return HttpResponse(f"La multiplicacion de {n1} * {n2} = {multiplicar}")

def dividir(request, n1, n2):
    dividir = n1 / n2
    return HttpResponse(f"La division de {n1} / {n2} = {dividir}")
