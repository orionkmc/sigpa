from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import PermissionRequiredMixin
from planificacion.models import Seccion, SeccionPeriodo, Horarios,\
    DIA_CHOICES, HORA_CHOICES
from planificacion.forms import HorarioForm
import json


class HorarioView(PermissionRequiredMixin, View):
    permission_required = 'planificacion.view_horarios'

    def get(self, request, seccion):
        s = Seccion.objects.get(pk=seccion)
        sps = SeccionPeriodo.objects.filter(seccion=seccion)
        horario_form = HorarioForm(
            initial={
                'materias': sps
            }
        )
        materias = materias_generate(sps, s)
        return render(request, 'horarios/index.html', {
            's': s,
            'sps': sps,
            'horario_form': horario_form,
            'dias': DIA_CHOICES,
            'horas': HORA_CHOICES,
            'periodo': 98,
            'materias': json.dumps(materias),
        })

    def post(self, request, seccion):
        s = Seccion.objects.get(pk=seccion)
        sps = SeccionPeriodo.objects.filter(seccion=seccion)
        horario_form = HorarioForm(
            request.POST,
            initial={
                'materias': sps
            }
        )
        if horario_form.is_valid():
            hora_desde = horario_form.cleaned_data['hora_desde']
            hora_hasta = horario_form.cleaned_data['hora_hasta']

            sp = SeccionPeriodo.objects.get(
                pk=horario_form.cleaned_data['materia']
            )
            # sp.horarios_seccion_periodo.all().delete()
            # for x in range(int(hora_desde), int(hora_hasta) + 1):
            Horarios(
                seccion_periodo=sp,
                dia=horario_form.cleaned_data['dia'],
                desde=hora_desde,
                hasta=hora_hasta,
                salon=horario_form.cleaned_data['salon'],
            ).save()

        materias = materias_generate(sps, s)
        return render(request, 'horarios/index.html', {
            's': s,
            'sps': sps,
            'horario_form': horario_form,
            'dias': DIA_CHOICES,
            'horas': HORA_CHOICES,
            'periodo': 98,
            'materias': json.dumps(materias),
        })


def materias_generate(sps, s):
    hs = Horarios.objects.filter(
        seccion_periodo__in=s.seccionperiodo_set.all()
    )
    materias = []
    for h in hs:
        sp = h.seccion_periodo
        try:
            try:
                s = sp.horarios_seccion_periodo.all(
                )[0].salon.piso.edificio.codigo
            except:
                s = ''
            salon = '{}{}'.format(
                s,
                sp.horarios_seccion_periodo.all()[0]
                    .salon.codigo
            )
            materias.append({
                'unidad_curricular': sp.unidad_curricular.nombre,
                'docente': {
                    'nombre': sp.docentes.nombre,
                    'apellido': sp.docentes.apellido
                },
                'seccion': sp.seccion.nombre,
                'salon': salon,
                'dia': h.dia,
                'desde': h.desde,
                'hasta': h.hasta,
                'cant': (int(h.hasta) - int(h.desde)) + 1,
            })
        except:
            materias.append({
                'unidad_curricular': '',
                'docente': {
                    'nombre': '',
                    'apellido': ''
                },
                'seccion': '',
                'salon': '',
                'first_dia': '',
                'first_hora': '',
                'cant': '',
            })
    return materias
