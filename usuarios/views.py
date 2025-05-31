# crm/usuarios/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import UsuarioPerfilForm
from django.contrib.auth.decorators import login_required 

@login_required
def login_view(request):
    """
    Muestra el formulario de login. Si POST es válido, autentica al usuario y lo redirige.
    """
    if request.method == 'POST':
        # usamos el AuthenticationForm de Django
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            # Recupera usuario y contraseña limpios
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            # authenticate() buscará el usuario en la base de datos
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)  # establece la sesión
                return redirect('dashboard')
            else:
                messages.error(request, 'Credenciales inválidas')
        else:
            messages.error(request, 'Datos de login inválidos')
    else:
        # Si es GET, simplemente creamos un formulario vacío
        form = AuthenticationForm()
    return render(request, 'usuarios/login.html', {'form': form})

def logout_view(request):
    """
    Cierra la sesión y redirige a la página indicada en LOGOUT_REDIRECT_URL.
    """
    logout(request)
    return redirect('dashboard')


def perfil_view(request):
    """
    Permite al usuario ver y editar su propio perfil:
    nombre, apellidos, email. También incluiremos un enlace
    para cambiar contraseña.
    """
    user = request.user

    if request.method == 'POST':
        # Pasamos request.POST y el instance=request.user para editarlo
        form = UsuarioPerfilForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Tu perfil se ha actualizado correctamente.")
            return redirect('perfil')
    else:
        form = UsuarioPerfilForm(instance=user)

    return render(request, 'usuarios/perfil.html', {'form': form})
