from django.shortcuts import render, get_object_or_404, redirect
from .models import Obra
from .forms import ObraForm

def listado_obras(request):
    obras = Obra.objects.all()
    return render(request, 'obras/listado_obras.html', {'obras': obras})

def crear_obra(request):
    if request.method == 'POST':
        form = ObraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listado_obras')
    else:
        form = ObraForm()
    return render(request, 'obras/crear_obra.html', {'form': form})

def editar_obra(request, obra_id):
    obra = get_object_or_404(Obra, pk=obra_id)
    if request.method == 'POST':
        form = ObraForm(request.POST, instance=obra)
        if form.is_valid():
            form.save()
            return redirect('listado_obras')
    else:
        form = ObraForm(instance=obra)
    return render(request, 'obras/editar_obra.html', {'form': form})

def eliminar_obra(request, obra_id):
    obra = get_object_or_404(Obra, pk=obra_id)
    if request.method == 'POST':
        obra.delete()
        return redirect('listado_obras')
    return render(request, 'obras/eliminar_obra.html', {'obra': obra})
