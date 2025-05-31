# crm/usuarios/urls.py

from django.urls import path
from .views import perfil_view, logout_view  # suponiendo que tienes un logout personalizado

urlpatterns = [
    # /usuarios/perfil/  → perfil del usuario (vista protegida con @login_required)
    path('perfil/', perfil_view, name='perfil'),
    # /usuarios/logout/  → logout (si lo manejas con una vista propia)
    path('logout/', logout_view, name='logout'),

    # Nota: NO pongas aquí ninguna ruta 'login/' ni 'password_change/' (estas vendrán de django.contrib.auth.urls).
]
