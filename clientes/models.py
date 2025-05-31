# clientes/models.py

from django.db import models

class Cliente(models.Model):
    # Opciones para tipo de cliente
    TIPO_CLIENTE = [
        ('P', 'Particular'),
        ('E', 'Empresa'),
    ]

    tipo = models.CharField(
        max_length=1,
        choices=TIPO_CLIENTE,
        default='P',
        verbose_name='Tipo de cliente'
    )
    nombre = models.CharField(
        max_length=100,
        verbose_name='Nombre / Razón social'
    )
    persona_contacto = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='Persona de contacto'
    )
    telefono_fijo = models.CharField(
        max_length=20,
        blank=True,
        verbose_name='Teléfono fijo'
    )
    telefono_movil = models.CharField(
        max_length=20,
        blank=True,
        verbose_name='Teléfono móvil'
    )
    email = models.EmailField(
        verbose_name='Correo electrónico'
    )

    # Dirección desglosada
    calle = models.CharField(
        max_length=200,
        blank=True,
        verbose_name='Calle y número'
    )
    ciudad = models.CharField(
        max_length=100,
        blank=True
    )
    provincia = models.CharField(
        max_length=100,
        blank=True
    )
    codigo_postal = models.CharField(
        max_length=10,
        blank=True,
        verbose_name='Código postal'
    )
    pais = models.CharField(
        max_length=100,
        default='España'
    )

    cif_nif = models.CharField(
        max_length=20,
        blank=True,
        verbose_name='CIF / NIF'
    )

    # Datos adicionales
    fecha_nacimiento = models.DateField(
        blank=True,
        null=True,
        verbose_name='Fecha de nacimiento'
    )
    fecha_creacion = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Fecha de alta'
    )
    notas_comerciales = models.TextField(
        blank=True,
        verbose_name='Notas / Comentarios'
    )

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['nombre']
