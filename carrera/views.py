from django.shortcuts import render
from django.views.generic import View
from carrera.models import UnidadCurricular, Malla, Subestructura, SubSubEstructura, MallaUCE
from carrera.forms import UnidadCurricularForm, MallaForm, MallauceForm
from django.forms.models import inlineformset_factory


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
        from django.forms import formset_factory
        malla_form = MallaForm()
        mallauce_formset = formset_factory(MallauceForm, extra=2)

        subestructuras = Subestructura.objects.all()
        # for subestructura in subestructuras:
        #     for tt in subestructura.tt.all():
        #         for muce in tt.malla_uce_sub_sub_estructura.all():
        #             mallauceform = MallauceForm(instance=muce)
        context = {
            'malla_form': malla_form,
            'subestructuras': subestructuras,
            'mallauceform': mallauce_formset,
        }
        return render(request, 'malla/add_malla.html', context)

    def post(self, request):
        malla_form = MallaForm()
        subestructuras = Subestructura.objects.all()
        context = {
            'malla_form': malla_form,
            'subestructuras': subestructuras,
        }
        return render(request, 'malla/add_malla.html', context)


class EditMallaView(View):
    def get(self, request, malla):
        malla = Malla.objects.get(pk=malla)
        malla_form = MallaForm(instance=malla)

        subestructuras = Subestructura.objects.all()
        context = {
            'malla_form': malla_form,
            'subestructuras': subestructuras,
        }
        return render(request, 'malla/edit_malla.html', context)

    def post(self, request, malla):
        malla = Malla.objects.get(pk=malla)

        MallauceFormFormSet = inlineformset_factory(
            SubSubEstructura, MallaUCE, extra=0, can_delete=True)

        malla_form = MallaForm(request.POST, instance=malla)

        if malla_form.is_valid():
            m = malla_form.save()
        mallauce_form_form_set = MallauceFormFormSet(request.POST, instance=m)
        print(mallauce_form_form_set)
        # print(mallauce_form_form_set)
        # if mallauce_form_form_set.is_valid():
        #     print(mallauce_form_form_set)
        # for form in formset:
        #     print(form)
        # for mallauce_pk in request.POST.getlist('mallauce_pk'):
        #     mallauce = MallaUCE.objects.get(pk=mallauce_pk)
        #     malla_form = MallaForm(request.POST, instance=mallauce)
        #     print(malla_form.is_valid)

        subestructuras = Subestructura.objects.all()
        context = {
            'malla_form': malla_form,
            'subestructuras': subestructuras,
        }
        return render(request, 'malla/edit_malla.html', context)

    def form_valid(self, form, mallauce_form_form_set):
        print(form)
        self.object = form.save()
        mallauce_form_form_set.instance = self.object
        mallauce_form_form_set.save()
        return True

    def form_invalid(self, form, mallauce_form_form_set):
        return False
