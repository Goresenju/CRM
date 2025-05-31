# clientes/forms.py

from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'tipo',
            'nombre',
            'persona_contacto',
            'telefono_fijo',
            'telefono_movil',
            'email',
            'calle',
            'ciudad',
            'provincia',
            'codigo_postal',
            'pais',
            'cif_nif',
            'fecha_nacimiento',
            'notas_comerciales',
        ]

        labels = {
            'tipo': 'Tipo de cliente',
            'nombre': 'Nombre / Razón social',
            'persona_contacto': 'Persona de contacto',
            'telefono_fijo': 'Teléfono fijo',
            'telefono_movil': 'Teléfono móvil',
            'email': 'Correo electrónico',
            'calle': 'Calle y número',
            'ciudad': 'Ciudad',
            'provincia': 'Provincia',
            'codigo_postal': 'Código postal',
            'pais': 'País',
            'cif_nif': 'CIF / NIF',
            'fecha_nacimiento': 'Fecha de nacimiento',
            'notas_comerciales': 'Notas / Comentarios',
        }

        widgets = {
            'tipo': forms.Select(attrs={'class': 'form-select'}),
            'nombre': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Ej. “Construcciones López S.L.” o “Juan Pérez”'
            }),
            'persona_contacto': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Ej. “María García”'
            }),
            'telefono_fijo': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Ej. 91 123 45 67'
            }),
            'telefono_movil': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Ej. 600 123 456'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'correo@ejemplo.com'
            }),
            'calle': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Calle y número (p.ej. “C/ Mayor, 10”)'
            }),
            'ciudad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Madrid'}),
            'provincia': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Madrid'}),
            'codigo_postal': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '28001'}),
            'pais': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'España'}),
            'cif_nif': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'CIF o NIF'
            }),
            'fecha_nacimiento': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'notas_comerciales': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 3,
                'placeholder': 'Escribe aquí cualquier comentario relevante…'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Autofocus en el campo “nombre” cuando se carga el formulario
        self.fields['nombre'].widget.attrs['autofocus'] = True
