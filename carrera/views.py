from django.shortcuts import render
from django.views.generic import View
# from django.forms.models import inlineformset_factory
from django.views.generic.detail import DetailView

from carrera.models import UnidadCurricular, Malla, Subestructura
from carrera.forms import UnidadCurricularForm, MallaForm, MallauceForm
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.exceptions import PermissionDenied


class UnidadCurricularDetailView(PermissionRequiredMixin, DetailView):
    permission_required = 'carrera.view_unidadcurricular'
    model = UnidadCurricular
    template_name = 'u_curricular/detail_u_curricular.html'


class UnidadesCurricularesView(PermissionRequiredMixin, View):
    permission_required = 'carrera.view_unidadcurricular'

    def get(self, request):
        unidades_curriculares = UnidadCurricular.objects.all()
        context = {
            'unidades_curriculares': unidades_curriculares,
        }
        return render(
            request,
            'u_curricular/u_curriculares.html', context)

    def post(self, request):
        if not request.user.has_perm('carrera.delete_unidadcurricular'):
            raise PermissionDenied
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
        return render(
            request,
            'u_curricular/u_curriculares.html', context)


class AddUnidadCurricularView(PermissionRequiredMixin, View):
    permission_required = 'carrera.add_unidadcurricular'

    def get(self, request):
        unidad_curricular_form = UnidadCurricularForm()
        context = {
            'unidad_curricular_form': unidad_curricular_form,
        }
        return render(
            request, 'u_curricular/add_u_curricular.html', context)

    def post(self, request):
        alert = False
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
            request, 'u_curricular/add_u_curricular.html', context)


class EditUnidadCurricularView(PermissionRequiredMixin, View):
    permission_required = 'carrera.change_unidadcurricular'

    def get(self, request, uc):
        uc = UnidadCurricular.objects.get(pk=uc)
        unidad_curricular_form = UnidadCurricularForm(instance=uc)
        context = {
            'unidad_curricular_form': unidad_curricular_form,
        }
        return render(
            request, 'u_curricular/edit_u_curricular.html', context)

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
            request, 'u_curricular/edit_u_curricular.html', context)


class MallasView(PermissionRequiredMixin, View):
    permission_required = 'carrera.view_malla'

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
        return render(
            request, 'u_curricular/u_curriculares.html', context)


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


class EditMallaView(PermissionRequiredMixin, View):
    permission_required = 'carrera.view_malla'

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

        # MallauceFormFormSet = inlineformset_factory(
        #     SubSubEstructura, MallaUCE, extra=0, can_delete=True)

        malla_form = MallaForm(request.POST, instance=malla)

        # if malla_forXmalla_form.save()
        # mallauce_form_form_set = MallauceFormFormSet(
        #     request.POST, instance=m)
        # print(mallauce_form_form_set)
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
