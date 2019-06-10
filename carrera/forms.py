# -*- coding: utf-8 -*-
from django import forms
from carrera.models import UnidadCurricular, Malla, MallaUCE


class UnidadCurricularForm(forms.ModelForm):
    class Meta:
        model = UnidadCurricular
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(UnidadCurricularForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] =\
                'form-control form-control-sm'


class MallaForm(forms.ModelForm):
    class Meta:
        model = Malla
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(MallaForm, self).__init__(*args, **kwargs)
        code = self.fields['cod'].widget
        code.attrs['class'] = 'form-control form-control-sm'
        code.attrs['placeholder'] = 'Codigo'


class MallauceForm(forms.ModelForm):
    class Meta:
        model = MallaUCE
        fields = ('horas_teoricas', 'horas_practicas', 'laboratorio')
        widgets = {
            'horas_teoricas': forms.TextInput(attrs={
                'class': 'form-control form-control-sm',
                'placeholder': 'Horas Teoricas',
            }),
            'horas_practicas': forms.TextInput(attrs={
                'class': 'form-control form-control-sm',
                'placeholder': 'Horas Practicas',
            }),
        }
