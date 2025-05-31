# crm/clientes/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente
from .forms import ClienteForm

def listado_clientes(request):
    """
    Muestra la lista de todos los clientes.
    """
    clientes = Cliente.objects.all()
    return render(request, 'clientes/listado_clientes.html', {'clientes': clientes})


def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listado_clientes')  # <-- usa el mismo name que definiremos abajo
    else:
        form = ClienteForm()
    return render(request, 'clientes/crear_cliente.html', {'form': form})


def editar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('listado_clientes')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'clientes/editar_cliente.html', {'form': form, 'cliente': cliente})


def eliminar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('listado_clientes')
    return render(request, 'clientes/eliminar_cliente.html', {'cliente': cliente})
