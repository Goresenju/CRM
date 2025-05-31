from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='clientes_inicio'),
]
