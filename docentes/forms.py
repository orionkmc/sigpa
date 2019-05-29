# -*- coding: utf-8 -*-
from django.forms import ModelForm
from docentes.models import Docentes


class DocenteForm(ModelForm):
    class Meta:
        model = Docentes
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(DocenteForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] =\
                'form-control form-control-sm'
