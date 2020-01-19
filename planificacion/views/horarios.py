from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import PermissionRequiredMixin
from planificacion.models import DIA_CHOICES, HORA_CHOICES
from planificacion.models import SeccionPeriodo
import json


class HorarioView(PermissionRequiredMixin, View):
    permission_required = 'planificacion.view_horarios'

    def get(self, request, seccion):
        sps = SeccionPeriodo.objects.filter(seccion=seccion)

        materias = []
        for sp in sps:
            if sp.horarios_seccion_periodo.all():
                first = sp.horarios_seccion_periodo.all().first()

                # last = sp.horarios_seccion_periodo.all().last()
                cant = sp.horarios_seccion_periodo.all().count()
                try:
                    salon = '{} {}'.format(
                        sp.horarios_seccion_periodo.all()[0]
                            .salon.piso.edificio.codigo,
                        sp.horarios_seccion_periodo.all()[0]
                            .salon.codigo
                    )
                    try:
                        docente = {
                            'nombre': sp.docentes.nombre,
                            'apellido': sp.docentes.apellido
                        }
                    except:
                        docente = {
                            'nombre': 'Docente',
                            'apellido': 'Sin'
                        }
                    materias.append({
                        'unidad_curricular': sp.unidad_curricular.nombre,
                        'docente': docente,
                        'seccion': sp.seccion.codigo,
                        'salon': salon,
                        'first_dia': first.dia,
                        'first_hora': first.hora,
                        'cant': cant,
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
        return render(request, 'horarios/index.html', {
            'seccion': seccion,
            'dias': DIA_CHOICES,
            'horas': HORA_CHOICES,
            'periodo': 98,
            'materias': json.dumps(materias),
        })
