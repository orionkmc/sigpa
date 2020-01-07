from django.shortcuts import render
from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from planificacion.forms import PeriodoForm, MallaForm
from carrera.models import SubSubEstructura
from planificacion.models import MallaUCEPeriodo, Periodo, Seccion,\
    SeccionPeriodo
# from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from docentes.models import Docentes

SECCION_CHOICES = (
    ('A'), ('B'), ('C'), ('D'),
    ('E'), ('F'), ('G'), ('H'),
    ('I'), ('J'), ('K'), ('L'),
    ('M'), ('N'), ('O'), ('P'),
    ('Q'), ('R'), ('S'), ('T'),
    ('U'), ('V'), ('W'), ('X'),
    ('Y'), ('Z'),
)


# # # # # # # # # # # # # # # # # # # # # # # #
#                  PERIODOS                   #
# # # # # # # # # # # # # # # # # # # # # # # #
class PeriodosView(ListView):
    model = Periodo


class PeriodoView(DetailView):
    model = Periodo


class PlanificacionView(View):
    def get(self, request):
        periodo = False
        if request.GET.get('periodo'):
            periodo = Periodo.objects.get(pk=request.GET.get('periodo'))

        periodo_form = PeriodoForm()
        malla_form = MallaForm()
        context = {
            'periodo_form': periodo_form,
            'malla_form': malla_form,
            'periodo': periodo,
        }
        return render(request, 'planificacion/periodo_agregar.html', context)

    def post(self, request):
        periodo = False
        if request.GET.get('periodo'):
            periodo = Periodo.objects.get(pk=request.GET.get('periodo'))

        periodo_form = PeriodoForm(request.POST)
        malla_form = MallaForm(request.POST)
        if periodo_form.is_valid():
            secciones = request.POST.getlist('secciones[]')
            tt = request.POST.getlist('tt[]')
            type_seccion = request.POST.getlist('type_seccion[]')
            print(type_seccion)
            p = periodo_form.save()

            for idx, seccion in enumerate(secciones):
                sse = SubSubEstructura.objects.get(pk=tt[idx])
                mucep = MallaUCEPeriodo(
                    trimestre=sse, periodo=p, secciones=seccion)
                mucep.save()
                for x in range(0, int(seccion)):
                    codigo = "{}-{}-{}-{}".format(
                        request.POST.get('codigo'),
                        sse,
                        SECCION_CHOICES[x],
                        type_seccion[idx]
                    )
                    s = Seccion(
                        codigo=codigo,
                        nombre=SECCION_CHOICES[x],
                        periodo=mucep)
                    s.save()
                    malla_uce = mucep.trimestre.malla_uce_ss_estruct.all()
                    for x in malla_uce:
                        SeccionPeriodo(
                            seccion=s,
                            unidad_curricular=x.unidad_credito,
                        ).save()
            periodo_form = PeriodoForm()
        context = {
            'periodo_form': periodo_form,
            'malla_form': malla_form,
            'periodo': periodo,
        }
        return render(request, 'planificacion/periodo_agregar.html', context)


class PlanificacionPlanillasView(View):
    def get(self, request, pk):
        from django.db.models import Count, Q

        sp = SeccionPeriodo.objects.filter(seccion__periodo__periodo__pk=pk)

        # Personal Docente Contratado
        dsc = Docentes.objects.annotate(dcount=Count('pk')).filter(
            Q(seccion_periodo_docente__seccion__periodo__periodo__pk=pk) |
            Q(seccion_periodo_docente_suplente__seccion__periodo__periodo__pk=pk),
            status='Contratado',
        )

        # Personal Docente Ordinario
        dso = Docentes.objects.annotate(dcount=Count('pk')).filter(
            Q(seccion_periodo_docente__seccion__periodo__periodo__pk=pk) |
            Q(seccion_periodo_docente_suplente__seccion__periodo__periodo__pk=pk),
            status='Ordinario',
        )

        # Otros
        sp_sp = SeccionPeriodo.objects.filter(
            docentes__pk=None,
            seccion__periodo__periodo__pk=pk
        )

        return render(request, 'planificacion/planificacion.html', {
            'pk_periodo': pk,
            'sp': sp,
            'dsc': dsc,
            'dso': dso,
            'sp_sp': sp_sp,
        })
