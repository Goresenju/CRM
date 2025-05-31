from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'telefono', 'email', 'direccion', 'cif_nif', 'notas']
        widgets = {
            'notas': forms.Textarea(attrs={'rows': 3}),
        }
