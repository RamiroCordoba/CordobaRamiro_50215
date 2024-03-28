from django import forms
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class HistoriaForm(forms.Form):
    titulo = forms.CharField(max_length=70, required=True)
    historia = forms.CharField(widget=forms.Textarea)


class RecetaForm(forms.Form):
    titulo = forms.CharField(max_length=70, required=True)
    descripcion = forms.CharField()
    ingredientes = forms.CharField(widget=forms.Textarea)
    instrucciones = forms.CharField(widget=forms.Textarea)


class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput())
    password2 = forms.CharField(
        label="Repetir Contraseña", widget=forms.PasswordInput()
    )

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        ]


class UserEditForm(UserChangeForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(label="Nombre/s", max_length=50, required=True)
    last_name = forms.CharField(label="Apellido/s", max_length=50, required=True)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]


class AvatarForm(forms.Form):
    imagen = forms.ImageField(required=True)
