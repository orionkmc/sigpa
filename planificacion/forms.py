# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm, ModelChoiceField
from django.forms.models import inlineformset_factory

from carrera.models import Subestructura
from planificacion.models import Periodo, Seccion, TURNO_CHOICES, Horarios
from docentes.models import Docentes
from planificacion.models import SeccionPeriodo
from plantaFisica.models import Salon


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
    # malla = forms.ModelChoiceField(
    #     queryset=Malla.objects.all(),
    #     empty_label="Mallas Academicas",
    #     required=False,
    #     widget=forms.Select(
    #         attrs={'class': 'form-control form-control-sm'},
    #     )
    # )
    subestructura = forms.ModelChoiceField(
        queryset=Subestructura.objects.all(), label="Trayectos",
        empty_label="Selecciona un Trayecto",
        required=False, widget=forms.Select(
            attrs={'class': 'form-control form-control-sm'},
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


DIA_CHOICES = (
    ('', '------'),
    ('Lunes', 'Lunes'),
    ('Martes', 'Martes'),
    ('Miercoles', 'Miercoles'),
    ('Jueves', 'Jueves'),
    ('Viernes', 'Viernes'),
    ('Sabado', 'Sabado'),
    ('Domingo', 'Domingo'),
)

HORA_CHOICES = (
    ('', '------'),
    ('1', '07:00 a 07:45'),
    ('2', '07:45 a 08:30'),
    ('3', '08:40 a 09:25'),
    ('4', '09:25 a 10:10'),
    ('5', '10:20 a 11:05'),
    ('6', '11:05 a 11:50'),
    ('7', '11:50 a 12:45'),
    ('8', '12:45 a 01:30'),
    ('9', '01:30 a 02:25'),
    ('10', '02:25 a 03:10'),
    ('11', '03:10 a 03:55'),
    ('12', '04:05 a 04:50'),
    ('13', '04:50 a 05:35'),
    ('14', '05:45 a 06:30'),
)


class MyModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        try:
            s = obj.piso.edificio.codigo
        except:
            s = ''
        return '{}{}'.format(
            s,
            obj.codigo
        )


class SeccionPeriodoForm(ModelForm):

    class Meta:
        model = SeccionPeriodo
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(SeccionPeriodoForm, self).__init__(*args, **kwargs)

        self.fields['unidad_curricular'].widget = forms.HiddenInput()
        for field in self.fields:
            self.fields[field].widget.attrs['form'] = 'save_seccion_periodo'
        self.fields['docentes'].\
            widget.attrs['class'] = 'form-control select2'
        self.fields['docentes'].required = True
        self.fields['suplente'].\
            widget.attrs['class'] = 'form-control select2'

        self.fields['horas_teoricas'].\
            widget.attrs['class'] = 'form-control form-control-sm'
        self.fields['horas_practicas'].\
            widget.attrs['class'] = 'form-control form-control-sm'


class HorarioForm(forms.Form):

    salon = MyModelChoiceField(
        queryset=Salon.objects.all(),
        empty_label="Selecciona un Salon",
        widget=forms.Select(
            attrs={'class': 'form-control form-control-sm select2'},
        ),
        required=True
    )
    dia = forms.CharField(
        label="Dia", required=True, widget=forms.Select(
            attrs={'class': 'form-control form-control-sm'},
            choices=DIA_CHOICES
        ))
    hora_desde = forms.CharField(
        label="Hora Desde", required=True, widget=forms.Select(
            attrs={'class': 'form-control form-control-sm'},
            choices=HORA_CHOICES,
        ))

    hora_hasta = forms.CharField(
        label="Hora Hasta", required=True, widget=forms.Select(
            attrs={'class': 'form-control form-control-sm'},
            choices=HORA_CHOICES,
        ))

    def __init__(self, *args, **kwargs):
        super(HorarioForm, self).__init__(*args, **kwargs)
        initial = kwargs.get('initial', None)
        data = [(m.pk, m.unidad_curricular.nombre)
                for m in initial['materias']]
        self.fields['materia'] = forms.ChoiceField(
            label=u'Materias',
            choices=data,
            widget=forms.Select(
                attrs={'class': 'form-control form-control-sm'}
            ),
            required=False
        )

    def clean(self):
        cleaned_data = super().clean()

        sp = SeccionPeriodo.objects.get(
            pk=cleaned_data.get("materia")
        )
        try:
            h = Horarios.objects.get(
                salon=cleaned_data.get("salon"),
                dia=cleaned_data.get("dia"),
                desde=cleaned_data.get("hora_desde"),
            )
            self.add_error(
                'hora_desde', 'Salon, Dia, Hora ocupado.')
        except Exception as e:
            print(e)
SeccionPeriodoFormSet = inlineformset_factory(
    Seccion,
    SeccionPeriodo,
    form=SeccionPeriodoForm,
    extra=0,
    can_delete=False,
)
