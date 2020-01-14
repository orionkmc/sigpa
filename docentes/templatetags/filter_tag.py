from django import template
from django.db.models import Q
from planificacion.models import SeccionPeriodo
from carrera.models import UnidadCurricular
from planificacion.models import Horarios, DIA_CHOICES, HORA_CHOICES
register = template.Library()


@register.inclusion_tag('partial/unidades_curriculares.html')
def docente_periodo_seccion(docente, pk_docente, pk_periodo):
    try:
        sp = SeccionPeriodo.objects.filter(
            Q(docentes__pk=pk_docente) |
            Q(suplente__pk=pk_docente),
            seccion__periodo__periodo__pk=pk_periodo
        )
        return {
            'docente': docente,
            'sp': sp,
        }

    except:
        return {}


@register.simple_tag
def total_horas_academicas(sp):
    horas_total = 0
    for x in sp:
        horas_total += x.horas_semanales
    return horas_total


@register.simple_tag
def unidades_curricular(uc):
    uc = UnidadCurricular.objects.get(pk=uc)
    return uc.nombre
