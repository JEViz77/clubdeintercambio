
# usuarios/forms.py

from django import forms
from .models import Usuario

class RegistroForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(),
        label='Contraseña'
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(),
        label='Confirmar Contraseña'
    )

    class Meta:
        model = Usuario
        # Se incluyen los campos que deseas que el usuario complete
        fields = ['nombre', 'email','dni','password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return cleaned_data