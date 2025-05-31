# crm/obras/views.py

from django.shortcuts import render
from django.http import HttpResponse

def obras_inicio(request):
    """
    Vista mínima para verificar que /obras/ funciona.
    Más adelante podrás cambiarla para que liste las obras
    desde la base de datos.
    """
    # Por ahora devolvemos un texto sencillo:
    return HttpResponse("Obras - Inicio")


