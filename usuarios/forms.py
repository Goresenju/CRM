# crm/usuarios/forms.py

from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class UsuarioPerfilForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellidos',
            'email': 'Correo electrónico',
        }

        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Tu nombre',
                'autocomplete': 'given-name',
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Tus apellidos',
                'autocomplete': 'family-name',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'correo@ejemplo.com',
                'autocomplete': 'email',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Autofocus en el primer campo (nombre)
        self.fields['first_name'].widget.attrs['autofocus'] = True

        # Agregar clase 'is-invalid' o 'is-valid' tras validar (opcional)
        for field_name, field in self.fields.items():
            field.widget.attrs.setdefault('class', 'form-control')

    def clean_email(self):
        """
        Si el usuario está intentando cambiar su correo, comprobamos
        que no exista ya otro usuario con ese mismo email.
        """
        email = self.cleaned_data.get('email').strip().lower()
        qs = User.objects.filter(email__iexact=email)

        # Si estamos actualizando y el email no ha cambiado, no hacemos nada
        if self.instance and self.instance.email.lower() == email:
            return email

        # Si encontramos otro usuario con ese email, lanzamos error
        if qs.exists():
            raise ValidationError("Este correo ya está en uso por otro usuario.")
        return email
