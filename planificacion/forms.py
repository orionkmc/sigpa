# -*- coding: utf-8 -*-
from django import forms
from carrera.models import Malla
from planificacion.models import Periodo, Seccion, TURNO_CHOICES
from django.forms import ModelForm
from docentes.models import Docentes
from planificacion.models import SeccionPeriodo
from django.forms.models import inlineformset_factory


class SeccionForm(ModelForm):
    class Meta:
        model = Seccion
        fields = ('codigo', 'nombre', 'turno',)
        widgets = {
            'codigo': forms.TextInput(attrs={
                'class': 'form-control form-control-sm',
                'placeholder': 'Código',
            }),
            'nombre': forms.TextInput(attrs={
                'class': 'form-control form-control-sm',
                'placeholder': 'nombre',
            }),
            'turno': forms.Select(
                choices=TURNO_CHOICES,
                attrs={
                    'class': 'form-control form-control-sm',
                    'placeholder': 'Turno',
                }),
        }


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
    CHOICES_SUBESTRUCTURA = (
        ('', 'Selecciona una Malla'),
    )
    CHOICES_SUB_SUBESTRUCTURA = (
        ('', 'Selecciona un Trayecto'),
    )
    malla = forms.ModelChoiceField(
        queryset=Malla.objects.all(),
        empty_label="Mallas Academicas",
        required=False,
        widget=forms.Select(
            attrs={'class': 'form-control form-control-sm'},
        )
    )
    subestructura = forms.CharField(
        label="Trayectos", required=False, widget=forms.Select(
            attrs={'class': 'form-control form-control-sm'},
            choices=CHOICES_SUBESTRUCTURA
        ))
    sub_subestructura = forms.CharField(
        label="Trimestres", required=False, widget=forms.Select(
            attrs={'class': 'form-control form-control-sm'},
            choices=CHOICES_SUB_SUBESTRUCTURA
        ))


class DocenteForm(forms.Form):
    docente = forms.ModelChoiceField(
        queryset=Docentes.objects.all(),
        empty_label="Selecciona un Docente",
        widget=forms.Select(
            attrs={'class': 'form-control form-control-sm'},
        ),
        required=True
    )


class SeccionPeriodoForm(ModelForm):
    class Meta:
        model = SeccionPeriodo
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(SeccionPeriodoForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


SeccionPeriodoFormSet = inlineformset_factory(
    Seccion,
    SeccionPeriodo,
    form=SeccionPeriodoForm,
    extra=0,
    can_delete=False,
)
