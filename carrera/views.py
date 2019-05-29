from django.shortcuts import render
from django.views.generic import View
from carrera.models import UnidadCurricular, Malla
from carrera.forms import UnidadCurricularForm, MallaForm


class UnidadesCurricularesView(View):
    def get(self, request):
        unidades_curriculares = UnidadCurricular.objects.all()
        context = {
            'unidades_curriculares': unidades_curriculares,
        }
        return render(request, 'unidad_credito/unidades_credito.html', context)

    def post(self, request):
        alert = False
        try:
            d = UnidadCurricular.objects.get(pk=request.POST.get('uc'))
            a = d.delete()
            if a:
                alert = True
        except Exception as e:
            print(e)

        unidades_curriculares = UnidadCurricular.objects.all()
        context = {
            'unidades_curriculares': unidades_curriculares,
            'alert': alert,
        }
        return render(request, 'unidad_credito/unidades_credito.html', context)


class AddUnidadCurricularView(View):
    def get(self, request):
        unidad_curricular_form = UnidadCurricularForm()
        context = {
            'unidad_curricular_form': unidad_curricular_form,
        }
        return render(
            request, 'unidad_credito/add_unidad_credito.html', context)

    def post(self, request):
        unidad_curricular_form = UnidadCurricularForm(request.POST)
        if unidad_curricular_form.is_valid():
            unidad_curricular_form.save()
            unidad_curricular_form = UnidadCurricularForm()
            alert = True
        context = {
            'unidad_curricular_form': unidad_curricular_form,
            'alert': alert,
        }
        return render(
            request, 'unidad_credito/add_unidad_credito.html', context)


class EditUnidadCurricularView(View):
    def get(self, request, uc):
        uc = UnidadCurricular.objects.get(pk=uc)
        unidad_curricular_form = UnidadCurricularForm(instance=uc)
        context = {
            'unidad_curricular_form': unidad_curricular_form,
        }
        return render(
            request, 'unidad_credito/edit_unidad_credito.html', context)

    def post(self, request, uc):
        alert = False
        uc = UnidadCurricular.objects.get(pk=uc)
        unidad_curricular_form = UnidadCurricularForm(
            request.POST, instance=uc)
        if unidad_curricular_form.is_valid():
            unidad_curricular_form.save()
            unidad_curricular_form = UnidadCurricularForm(instance=uc)
            alert = True
        context = {
            'unidad_curricular_form': unidad_curricular_form,
            'alert': alert,
        }
        return render(
            request, 'unidad_credito/edit_unidad_credito.html', context)


class MallasView(View):
    def get(self, request):
        mallas = Malla.objects.all()
        context = {
            'mallas': mallas,
        }
        return render(request, 'malla/mallas.html', context)

    def post(self, request):
        alert = False
        try:
            d = UnidadCurricular.objects.get(pk=request.POST.get('uc'))
            a = d.delete()
            if a:
                alert = True
        except Exception as e:
            print(e)

        unidades_curriculares = UnidadCurricular.objects.all()
        context = {
            'unidades_curriculares': unidades_curriculares,
            'alert': alert,
        }
        return render(request, 'unidad_credito/unidades_credito.html', context)


class AddMallaView(View):
    def get(self, request):
        malla_form = MallaForm()
        context = {
            'malla_form': malla_form,
        }
        return render(request, 'malla/add_malla.html', context)
