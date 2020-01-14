from django.shortcuts import render
from django.views.generic import View
from planificacion.models import DIA_CHOICES, HORA_CHOICES
from planificacion.models import SeccionPeriodo
import json


class HorarioView(View):
    def get(self, request, seccion):
        sps = SeccionPeriodo.objects.filter(seccion=seccion)

        materias = []
        for sp in sps:
            if sp.horarios_seccion_periodo.all():
                first = sp.horarios_seccion_periodo.all().first()
                # last = sp.horarios_seccion_periodo.all().last()
                cant = sp.horarios_seccion_periodo.all().count()
                salon = '{} {}'.format(
                    sp.horarios_seccion_periodo.all()[0].salon.piso.edificio.codigo,
                    sp.horarios_seccion_periodo.all()[0].salon.codigo
                )
                materias.append({
                    'unidad_curricular': sp.unidad_curricular.nombre,
                    'docente': {
                        'nombre': sp.docentes.nombre,
                        'apellido': sp.docentes.apellido
                    },
                    'seccion': sp.seccion.codigo,
                    'salon': salon,
                    'first_dia': first.dia,
                    'first_hora': first.hora,
                    'cant': cant,
                })

        return render(request, 'horarios/index.html', {
            'seccion': seccion,
            'dias': DIA_CHOICES,
            'horas': HORA_CHOICES,
            'periodo': 98,
            'materias': json.dumps(materias),
        })
