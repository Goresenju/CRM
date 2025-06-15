from django.db import models
from clientes.models import Cliente

class Obra(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='obras')
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    direccion = models.CharField(max_length=200)
    fecha_inicio = models.DateField(null=True, blank=True)
    fecha_fin = models.DateField(null=True, blank=True)
    estado = models.CharField(
        max_length=20,
        choices=[
            ('pendiente', 'Pendiente'),
            ('en_progreso', 'En progreso'),
            ('finalizada', 'Finalizada')
        ],
        default='pendiente'
    )

    def __str__(self):
        return f"{self.nombre} ({self.cliente.nombre})"
