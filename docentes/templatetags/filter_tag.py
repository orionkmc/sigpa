from django import template
from planificacion.models import SeccionPeriodo
register = template.Library()


@register.inclusion_tag('partial/unidades_curriculares.html')
def docente_periodo_seccion(pk_docente, pk_periodo):
    try:
        sp = SeccionPeriodo.objects.filter(
            docentes__pk=pk_docente,
            seccion__periodo__periodo__pk=pk_periodo
        )
        return {'sp': sp}

    except:
        return {}
