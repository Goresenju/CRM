# crm/usuarios/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Ruta para mostrar el formulario de login y procesarlo
    path('login/', views.login_view, name='login'),

    # Ruta para cerrar sesión (logout)
    path('logout/', views.logout_view, name='logout'),
]
