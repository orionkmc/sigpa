from django.shortcuts import render, redirect
from django.views.generic import View
from planificacion.forms import DocenteForm, SeccionForm
from carrera.models import MallaUCE, UnidadCurricular
from docentes.models import Docentes
from planificacion.models import MallaUCEPeriodo, Periodo, Seccion,\
    SeccionPeriodo
# # # # # # # # # # # # # # # # # # # # # # # #
#                 SECCIONES                   #
# # # # # # # # # # # # # # # # # # # # # # # #


class AddSeccionView(View):
    def get(self, request, periodo, tt):
        periodo = Periodo.objects.get(pk=periodo)
        mp = MallaUCEPeriodo.objects.get(pk=tt)
        seccion_form = SeccionForm()
        context = {
            'periodo': periodo,
            'mp': mp,
            'seccion_form': seccion_form,
        }
        return render(request, 'secciones/add_seccion.html', context)

    def post(self, request, periodo, tt):
        periodo = Periodo.objects.get(pk=periodo)
        mp = MallaUCEPeriodo.objects.get(pk=tt)

        seccion_form = SeccionForm(request.POST)
        if seccion_form.is_valid():
            s_form = seccion_form.save(commit=False)
            s_form.periodo = mp
            s_form.save()

            return redirect('secciones', periodo.pk)
        context = {
            'periodo': periodo,
            'mp': mp,
            'seccion_form': seccion_form,
        }
        return render(request, 'secciones/add_seccion.html', context)


class SeccionesView(View):
    def get(self, request, periodo):
        malla_periodo = MallaUCEPeriodo.objects.filter(periodo=periodo)
        context = {
            'malla_periodo': malla_periodo
        }
        return render(request, 'secciones/secciones.html', context)

    def post(self, request, periodo):
        alert = False
        malla_periodo = MallaUCEPeriodo.objects.filter(
            periodo=periodo)
        try:
            d = Seccion.objects.get(pk=request.POST.get('seccion'))
            a = d.delete()
            if a:
                alert = True
        except Exception as e:
            print(e)

        context = {
            'alert': alert,
            'malla_periodo': malla_periodo,
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
