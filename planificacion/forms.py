# -*- coding: utf-8 -*-
from django import forms
# from carrera.models import Malla
from planificacion.models import Periodo
from django.forms import ModelForm
# from docentes.models import Docentes


class PeriodoForm(ModelForm):
    class Meta:
        model = Periodo
        fields = ('codigo', 'nombre', 'fecha_inicio', 'fecha_fin')
        widgets = {
            'codigo': forms.TextInput(attrs={
                'class': 'form-control form-control-sm',
                'placeholder': 'Codigo',
            }),
            'nombre': forms.TextInput(attrs={
                'class': 'form-control form-control-sm',
                'placeholder': 'nombre',
            }),
            'fecha_inicio': forms.TextInput(attrs={
                'type': 'date',
                'class': 'form-control form-control-sm',
                'placeholder': 'Fecha de inicio',
            }),
            'fecha_fin': forms.TextInput(attrs={
                'type': 'date',
                'class': 'form-control form-control-sm',
                'placeholder': 'Fecha de fin',
            }),
        }


class MallaForm(forms.Form):
    CHOICES_MALLA = (
        ('', 'Mallas Academicas'),
        # ('', [(x.pk, x.cod) for x in Malla.objects.all()],),
    )

    CHOICES_SUBESTRUCTURA = (
        ('', 'Selecciona una Malla'),
    )
    CHOICES_SUB_SUBESTRUCTURA = (
        ('', 'Selecciona un Trayecto'),
    )

    malla = forms.CharField(
        label="Malla", widget=forms.Select(
            attrs={'class': 'form-control form-control-sm'},
            choices=CHOICES_MALLA
        ))
    subestructura = forms.CharField(
        label="Trayectos", widget=forms.Select(
            attrs={'class': 'form-control form-control-sm'},
            choices=CHOICES_SUBESTRUCTURA
        ))
    sub_subestructura = forms.CharField(
        label="Trimestres", widget=forms.Select(
            attrs={'class': 'form-control form-control-sm'},
            choices=CHOICES_SUB_SUBESTRUCTURA
        ))


class DocenteForm(forms.Form):
    CHOICES_DOCENTE = (
        ('', 'Selecciona un Docente'),
        # ('', [(x.pk, x.nombre) for x in Docentes.objects.all()],),
    )

    docente = forms.CharField(
        label="Docente", widget=forms.Select(
            attrs={'class': 'form-control form-control-sm'},
            choices=CHOICES_DOCENTE
        ), required=True)
