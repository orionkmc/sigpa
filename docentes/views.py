from django.views.generic import View
from django.shortcuts import render
from docentes.models import Docentes
from docentes.forms import DocenteForm


class DocentesView(View):
    def get(self, request):
        d = Docentes.objects.all()

        context = {
            'docentes': d,
        }
        return render(request, 'docentes/docentes.html', context)

    def post(self, request):
        alert = False
        try:
            d = Docentes.objects.get(pk=request.POST.get('docente'))
            a = d.delete()
            if a:
                alert = True
        except Exception as e:
            print(e)

        docentes = Docentes.objects.all()
        context = {
            'docentes': docentes,
            'alert': alert,
        }
        return render(request, 'docentes/docentes.html', context)


class AddDocenteView(View):
    def get(self, request):
        docente_form = DocenteForm()
        context = {
            'docente_form': docente_form,
        }
        return render(request, 'docentes/add_docente.html', context)

    def post(self, request):
        alert = False
        docente_form = DocenteForm(request.POST)
        if docente_form.is_valid():
            docente_form.save()
            docente_form = DocenteForm()
            alert = True
        context = {
            'docente_form': docente_form,
            'alert': alert,
        }
        return render(request, 'docentes/add_docente.html', context)


class EditDocenteView(View):
    def get(self, request, docente):
        d = Docentes.objects.get(pk=docente)
        docente_form = DocenteForm(instance=d)
        context = {
            'docente_form': docente_form,
        }
        return render(request, 'docentes/edit_docente.html', context)

    def post(self, request, docente):
        alert = False
        d = Docentes.objects.get(pk=docente)
        docente_form = DocenteForm(request.POST, instance=d)
        if docente_form.is_valid():
            docente_form.save()
            docente_form = DocenteForm(instance=d)
            alert = True
        context = {
            'docente_form': docente_form,
            'alert': alert,
        }
        return render(request, 'docentes/edit_docente.html', context)
