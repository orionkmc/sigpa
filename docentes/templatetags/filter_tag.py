from django import template
from planificacion.models import SeccionPeriodo
register = template.Library()


@register.inclusion_tag('partial/unidades_curriculares.html')
def docente_periodo_seccion(docente, pk_docente, pk_periodo):
    try:
        sp = SeccionPeriodo.objects.filter(
            docentes__pk=pk_docente,
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
