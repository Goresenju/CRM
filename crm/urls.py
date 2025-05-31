from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import dashboard

urlpatterns = [
    path('admin/', admin.site.urls),

    # Clientes (y otras apps que tengas):
    path('clientes/', include('clientes.urls')),
    # path('obras/', include('obras.urls')),
    # path('facturacion/', include('facturacion.urls')),
    # path('contabilidad/', include('contabilidad.urls')),

    # Login personalizado
    path(
        'usuarios/login/',
        auth_views.LoginView.as_view(template_name='usuarios/login.html'),
        name='login'
    ),

    # Resto de vistas de autenticación (logout, cambio de contraseña…)
    path('usuarios/', include('django.contrib.auth.urls')),

    # URLs propias de tu app "usuarios" (perfiles, logout custom, etc.)
    path('usuarios/', include('usuarios.urls')),

    # Dashboard
    path('', dashboard, name='dashboard'),
]
