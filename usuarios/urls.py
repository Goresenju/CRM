from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import perfil_view

urlpatterns = [
    # Vista de perfil protegida
    path('perfil/', perfil_view, name='perfil'),

    # Logout usando la vista integrada de Django con redirección al login
    path('logout/', LogoutView.as_view(next_page='/usuarios/login/'), name='logout'),
]
