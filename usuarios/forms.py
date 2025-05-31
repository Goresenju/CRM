# crm/usuarios/forms.py

from django import forms
from django.contrib.auth.models import User

class UsuarioPerfilForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'last_name':  forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellidos'}),
            'email':      forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo electrónico'}),
        }
