# crm/clientes/urls.py

from django.urls import path
from .views import (
    listado_clientes,
    crear_cliente,
    editar_cliente,
    eliminar_cliente,
)

urlpatterns = [
    # 1) Ruta para ver el listado de clientes (name='listado_clientes')
    path('', listado_clientes, name='listado_clientes'),

    # 2) Ruta para crear un cliente nuevo
    path('nuevo/', crear_cliente, name='crear_cliente'),

    # 3) Ruta para editar un cliente existente
    path('editar/<int:cliente_id>/', editar_cliente, name='editar_cliente'),

    # 4) Ruta para eliminar un cliente (confirmación GET + POST)
    path('eliminar/<int:cliente_id>/', eliminar_cliente, name='eliminar_cliente'),
]
