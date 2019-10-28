from io import BytesIO
from django.http import JsonResponse, HttpResponse
from carrera.models import Malla, Subestructura
from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import Table, Image
from carrera.models import SubSubEstructura, MallaUCE
from planificacion.models import MallaUCEPeriodo, Periodo
# from django.views.generic import TemplateView
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
