from django.shortcuts import render, redirect
from django.views.generic import View
from planificacion.forms import SeccionForm, SeccionPeriodoFormSet
from carrera.models import MallaUCE, UnidadCurricular
from planificacion.models import MallaUCEPeriodo, Periodo, Seccion,\
    SeccionPeriodo
from docentes.models import Docentes
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

            malla_uce = mp.trimestre.malla_uce_ss_estruct.all()
            for x in malla_uce:
                SeccionPeriodo(
                    seccion=s_form,
                    unidad_curricular=x.unidad_credito,
                ).save()

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
        seccion_periodo_form = SeccionPeriodoFormSet(instance=seccion)
        context = {
            'seccion': seccion,
            'muce': muce,
            'seccion_periodo_form': seccion_periodo_form,
            'docentes': Docentes.objects.all(),
            'unidadesC': UnidadCurricular.objects.all(),
        }
        return render(request, 'secciones/seccion.html', context)

    def post(self, request, periodo, seccion):
        seccion = Seccion.objects.get(pk=seccion)
        muce = MallaUCE.objects.filter(
            sub_sub_estructura=seccion.periodo.trimestre)

        if request.POST.get('seccion_periodo'):
            d = SeccionPeriodo.objects.get(
                pk=request.POST.get('seccion_periodo'))
            d.delete()
            seccion_periodo_form = SeccionPeriodoFormSet(instance=seccion)
        else:
            seccion_periodo_form = SeccionPeriodoFormSet(
                request.POST, instance=seccion
            )

            if seccion_periodo_form.is_valid():
                for form in seccion_periodo_form:
                    form.save()
        context = {
            'seccion': seccion,
            'muce': muce,
            'seccion_periodo_form': seccion_periodo_form,
            'docentes': Docentes.objects.all(),
            'unidadesC': UnidadCurricular.objects.all(),
        }
        return render(request, 'secciones/seccion.html', context)


class SeccionVerView(View):
    def get(self, request, periodo, seccion):
        s = Seccion.objects.get(pk=seccion)
        sps = SeccionPeriodo.objects.filter(seccion=s)

        context = {
            'periodo_pk': periodo,
            'seccion': s,
            'sps': sps,
        }
        return render(request, 'secciones/seccion_ver.html', context)
