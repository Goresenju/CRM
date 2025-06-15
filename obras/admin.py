from django.contrib import admin
from .models import Obra

@admin.register(Obra)
class ObraAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'cliente', 'fecha_inicio', 'fecha_fin', 'estado')
    search_fields = ('nombre', 'cliente__nombre')
    list_filter = ('estado',)
