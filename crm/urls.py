# crm/urls.py
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import dashboard

urlpatterns = [
    path('admin/', admin.site.urls),

    path('clientes/', include('clientes.urls')),

    path('usuarios/login/',
         auth_views.LoginView.as_view(template_name='usuarios/login.html'),
         name='login'),

    # 👇 Quitamos esta línea (ya tienes tus propias vistas de logout y perfil)
    # path('usuarios/', include('django.contrib.auth.urls')),

    # ✅ Mantenemos esta
    path('usuarios/', include('usuarios.urls')),

    path('', dashboard, name='dashboard'),
]
