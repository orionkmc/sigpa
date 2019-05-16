from io import BytesIO
from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse, HttpResponse
from planificacion.forms import PeriodoForm, MallaForm, DocenteForm

from carrera.models import Malla, Subestructura, SubSubEstructura,\
    MallaUCE, UnidadCurricular
from planificacion.models import MallaUCEPeriodo, Periodo, Seccion,\
    SeccionPeriodo
from docentes.models import Docentes

from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle
# from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import Table, Image

SECCION_CHOICES = (
    ('A'), ('B'), ('C'), ('D'),
    ('E'), ('F'), ('G'), ('H'),
    ('I'), ('J'), ('K'), ('L'),
    ('M'), ('N'), ('O'), ('P'),
    ('Q'), ('R'), ('S'), ('T'),
    ('U'), ('V'), ('W'), ('X'),
    ('Y'), ('Z'),
)


def home(request):
    context = {}
    return render(request, 'dashboard.html', context)


class PlanificacionView(View):
    def get(self, request):
        periodo_form = PeriodoForm()
        malla_form = MallaForm()
        context = {
            'periodo_form': periodo_form,
            'malla_form': malla_form
        }
        return render(request, 'planificacion/periodo_agregar.html', context)

    def post(self, request):
        periodo_form = PeriodoForm(request.POST)
        malla_form = MallaForm(request.POST)
        if periodo_form.is_valid():
            secciones = request.POST.getlist('secciones[]')
            tt = request.POST.getlist('tt[]')
            p = periodo_form.save()
            for idx, seccion in enumerate(secciones):
                sse = SubSubEstructura.objects.get(pk=tt[idx])
                mucep = MallaUCEPeriodo(
                    trimestre=sse, periodo=p, secciones=seccion)
                mucep.save()

            periodo_form = PeriodoForm()
        context = {
            'periodo_form': periodo_form,
            'malla_form': malla_form
        }
        return render(request, 'planificacion/periodo_agregar.html', context)


class PlanificacionPlanillasView(View):
    def get(self, request):
        periodos = Periodo.objects.all()
        context = {
            'periodos': periodos
        }
        return render(request, 'planificacion/periodos.html', context)
# # # # # # # # # # # # # # # # # # # # # # # #
#                  PERIODOS                   #
# # # # # # # # # # # # # # # # # # # # # # # #


class PeriodoView(View):
    def get(self, request, periodo):
        periodo = Periodo.objects.get(pk=periodo)
        mps = MallaUCEPeriodo.objects.filter(periodo=periodo)
        context = {
            'mps': mps,
            'periodo': periodo
        }
        return render(request, 'planificacion/periodo.html', context)


class PeriodosView(View):
    def get(self, request):
        periodos = Periodo.objects.all()
        context = {
            'periodos': periodos
        }
        return render(request, 'planificacion/periodos.html', context)


class PeriodoNuevoView(View):
    def get(self, request, periodo):
        periodo_form = PeriodoForm()
        periodo = Periodo.objects.get(pk=periodo)
        mps = MallaUCEPeriodo.objects.filter(periodo=periodo)
        # m = []
        # for mp in mps:
        #     print(mp.trimestre)
        #     print(mp.trimestre.parentId)
        #     m.append(mp.trimestre.pk)
        # m = set(m)
        # mm = list(m)
        # sse = SubSubEstructura.objects.filter(pk__in=mm)
        # for ss in sse:
        #     print(ss.parentId.malla_uce_sub_sub_estructura.all())
        context = {
            'mps': mps,
            'periodo': periodo,
            'periodo_form': periodo_form,
        }
        return render(request, 'planificacion/periodo_nuevo.html', context)

    def post(self, request, periodo):
        periodo_form = PeriodoForm(request.POST)
        periodo = Periodo.objects.get(pk=periodo)
        mps = MallaUCEPeriodo.objects.filter(periodo=periodo)
        mp_pk = []
        for mp in mps:
            mp_pk.append(mp.secciones)
            # m = set(m)
            mps_pk = list(mp_pk)

        if periodo_form.is_valid():
            tt = request.POST.getlist('tt[]')
            p = periodo_form.save()
            for idx, mp in enumerate(mps_pk):
                sse = SubSubEstructura.objects.get(pk=tt[idx])
                mucep = MallaUCEPeriodo(
                    trimestre=sse, periodo=p, secciones=mp)
                mucep.save()
                for x in range(0, mp):
                    s = Seccion(
                        codigo=SECCION_CHOICES[x],
                        nombre=SECCION_CHOICES[x],
                        periodo=mucep)
                    s.save()

            periodo_form = PeriodoForm()
        context = {
            'mps': mps,
            'periodo': periodo,
            'periodo_form': periodo_form,
        }
        return render(request, 'planificacion/periodo_nuevo.html', context)
# # # # # # # # # # # # # # # # # # # # # # # #
#                 SECCIONES                   #
# # # # # # # # # # # # # # # # # # # # # # # #


class SeccionesView(View):
    def get(self, request, periodo):
        malla_periodo = MallaUCEPeriodo.objects.filter(periodo=periodo)
        context = {
            'malla_periodo': malla_periodo
        }
        return render(request, 'secciones/secciones.html', context)


class SeccionView(View):
    def get(self, request, periodo, seccion):
        seccion = Seccion.objects.get(pk=seccion)
        muce = MallaUCE.objects.filter(
            sub_sub_estructura=seccion.periodo.trimestre)
        docentes = DocenteForm()

        context = {
            'seccion': seccion,
            'muce': muce,
            'docentes': docentes
        }
        return render(request, 'secciones/seccion.html', context)

    def post(self, request, periodo, seccion):
        seccion = Seccion.objects.get(pk=seccion)
        muce = MallaUCE.objects.filter(
            sub_sub_estructura=seccion.periodo.trimestre)

        docentes = DocenteForm(request.POST)
        if docentes.is_valid():
            ucs = request.POST.getlist('uc[]')
            d = request.POST.getlist('docente')

            for idx, uc in enumerate(ucs):
                docente = Docentes.objects.get(pk=d[idx])
                unidad_curricular = UnidadCurricular.objects.get(pk=uc)
                sp = SeccionPeriodo(
                    seccion=seccion,
                    docentes=docente,
                    unidad_curricular=unidad_curricular)
                sp.save()
        context = {
            'seccion': seccion,
            'muce': muce,
            'docentes': docentes
        }
        return render(request, 'secciones/seccion.html', context)


class SeccionVerView(View):
    def get(self, request, periodo, seccion):
        s = Seccion.objects.get(pk=seccion)
        sps = SeccionPeriodo.objects.filter(seccion=s)

        context = {
            'seccion': s,
            'sps': sps,
        }
        return render(request, 'secciones/seccion_ver.html', context)
# # # # # # # # # # # # # # # # # # # # # # # #
#                   AJAX                      #
# # # # # # # # # # # # # # # # # # # # # # # #


def trayecto(request):
    malla_id = request.GET.get('malla', None)
    malla = Malla.objects.get(pk=malla_id)
    ses = Subestructura.objects.filter(malla=malla)
    print(ses)
    response = {
        "status": True,
        "results": [
            {
                "pk": se.pk,
                "nombre": se.nombre
            }
            for se in ses
        ],
    }
    return JsonResponse(response)


def trimestre(request):
    trayecto_id = request.GET.get('trayecto', None)
    trayecto = Subestructura.objects.get(pk=trayecto_id)
    sses = SubSubEstructura.objects.filter(subestructura=trayecto)
    response = {
        "status": True,
        "results": [
            {
                "pk": sse.pk,
                "codigo": sse.codigo,
                "nombre": sse.nombre
            }
            for sse in sses
        ],
    }
    return JsonResponse(response)


def malla(request):
    trimestre_id = request.GET.get('trimestre', None)
    trimestre = SubSubEstructura.objects.get(pk=trimestre_id)

    malla_uce = MallaUCE.objects.filter(sub_sub_estructura=trimestre)
    # sses = SubSubEstructura.objects.filter(subestructura=trayecto)
    response = {
        "status": True,
        "sub_sub_estructura":
        trimestre.subestructura.nombre + ' ' + trimestre.nombre,
        "results": [
            {
                "pk": muce.pk,
                "unidad_credito": muce.unidad_credito.nombre,
                "horas": (muce.horas_teoricas + muce.horas_practicas),
            }
            for muce in malla_uce
        ],
    }
    return JsonResponse(response)


def header_footer(canvas, doc):
    # Save the state of our canvas so we can draw on it
    canvas.saveState()

    # Header
    archivo_imagen = 'http://localhost:8000/static/assets/img/ministerio.jpg'
    header = Image(archivo_imagen, width=200, height=40, hAlign='RIGHT')
    w, h = header.wrap(doc.width, doc.topMargin)
    header.drawOn(canvas, doc.leftMargin, doc.height + doc.topMargin - h)

    # styles = getSampleStyleSheet()
    style = ParagraphStyle(
        alignment=1,
        name='Normal',
        fontSize=6,
    )

    header_1 = Paragraph("Republica Bolivariana de Venezuela", style=style)
    w, h = header_1.wrap(doc.width, doc.topMargin)
    header_1.drawOn(canvas, 50, doc.height - 3 + doc.topMargin - h)

    header_2 = Paragraph(
        "Ministerio del Poder Popular para la"
        "Educación Universitaria, Ciencia y Tecnología", style=style)
    w, h = header_2.wrap(doc.width, doc.topMargin)
    header_2.drawOn(canvas, 50, doc.height - 8 + doc.topMargin - h)

    header_3 = Paragraph("PNF Informtica - Ejido (PNFI-2012)", style=style)
    w, h = header_3.wrap(doc.width, doc.topMargin)
    header_3.drawOn(canvas, 50, doc.height - 16 + doc.topMargin - h)

    header_4 = Paragraph(
        "Periodo Académico 2015-B (18/05/2015 - 04/03/2016)", style=style)
    w, h = header_4.wrap(doc.width, doc.topMargin)
    header_4.drawOn(canvas, 50, doc.height - 24 + doc.topMargin - h)

    archivo_imagen = 'http://localhost:8000/static/assets/img/logo.png'
    header = Image(archivo_imagen, width=50, height=50, hAlign='RIGHT')
    w, h = header.wrap(doc.width, doc.topMargin)

    header.drawOn(canvas, 710, doc.height + doc.topMargin - h)
    # Release the canvas
    canvas.restoreState()


def generar_pdf(request, periodo):
    response = HttpResponse(content_type='application/pdf')
    # pdf_name = "clientes.pdf"  # llamado clientes
    # response['Content-Disposition'] = 'attachment; filename=%s' % pdf_name
    buff = BytesIO()
    doc = SimpleDocTemplate(
        buff,
        pagesize=landscape(letter),
        rightMargin=40,
        leftMargin=40,
        topMargin=60,
        bottomMargin=18,
    )
    periodo = Periodo.objects.get(pk=periodo)

    clientes = []
    headings = ('Unidad Curricular', 'Nº Hora', 'Nº Sección', 'Total Horas')
    allperiodo = [
        (
            mp.malla_uce.unidad_credito.nombre,
            mp.malla_uce.horas_teoricas,
            mp.secciones,
            mp.malla_uce.horas_teoricas * mp.secciones,
        ) for mp in MallaUCEPeriodo.objects.filter(periodo=periodo)
    ]
    t = Table([headings] + allperiodo)
    t.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (3, -1), 1, colors.dodgerblue),
            ('LINEBELOW', (0, 0), (-1, 0), 2, colors.darkblue),
            ('BACKGROUND', (0, 0), (-1, 0), colors.dodgerblue)
        ]
    ))

    clientes.append(t)
    doc.build(clientes, onFirstPage=header_footer, onLaterPages=header_footer)

    response.write(buff.getvalue())
    buff.close()
    return response
