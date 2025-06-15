from django.urls import path
from . import views

urlpatterns = [
    path('', views.listado_obras, name='listado_obras'),
    path('crear/', views.crear_obra, name='crear_obra'),
    path('editar/<int:obra_id>/', views.editar_obra, name='editar_obra'),
    path('eliminar/<int:obra_id>/', views.eliminar_obra, name='eliminar_obra'),
]