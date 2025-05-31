# crm/urls.py (archivo principal de URLs)

from django.contrib import admin
from django.urls import path, include
from .views import dashboard
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clientes/', include('clientes.urls')),
    path('obras/', include('obras.urls')),
    path('facturacion/', include('facturacion.urls')),
    path('contabilidad/', include('contabilidad.urls')),
    path('usuarios/', include('django.contrib.auth.urls')),  # <-- Aquí incluimos las URLs de autentificación
    path('', dashboard, name='dashboard'),
     path(
        'usuarios/login/',
        auth_views.LoginView.as_view(
            template_name='usuarios/login.html'
        ),
        name='login'
    ),
]
