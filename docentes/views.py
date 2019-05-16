from django.views.generic import View
from django.shortcuts import render
from docentes.models import Docentes


class DocentesView(View):
    def get(self, request):
        d = Docentes.objects.all()

        context = {
            'docentes': d,
        }
        return render(request, 'docentes/docentes.html', context)
