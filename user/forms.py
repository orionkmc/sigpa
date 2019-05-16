# -*- coding: utf-8 -*-
from django import forms


class LoginForm(forms.Form):
    dni = forms.IntegerField(
        label='Cédula',
        widget=forms.TextInput(
            attrs={
                'id': 'cedula',
                'class': 'form-control',
                'type': 'number',
                'placeholder': 'Cédula',
            }
        ))
    password = forms.CharField(
        label='Contraseña', widget=forms.PasswordInput(
            attrs={
                'id': 'password',
                'class': 'form-control',
                'placeholder': 'Contraseña'
            }
        ))
