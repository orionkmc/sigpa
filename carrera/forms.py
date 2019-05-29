# -*- coding: utf-8 -*-
from django.forms import ModelForm
from carrera.models import UnidadCurricular, Malla


class UnidadCurricularForm(ModelForm):
    class Meta:
        model = UnidadCurricular
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(UnidadCurricularForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] =\
                'form-control form-control-sm'


class MallaForm(ModelForm):
    class Meta:
        model = Malla
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(MallaForm, self).__init__(*args, **kwargs)
        code_kuai = self.fields['cod'].widget
        code_kuai.attrs['class'] = 'form-control form-control-sm'
        code_kuai.attrs['placeholder'] = 'Codigo'
