from django.contrib import admin
# from docentes.models import Docentes, Pregrados, Postgrados, Telefono, Email,
#    PregradosDocente, PostgradosDocente
from docentes.models import Docentes, Telefono, Email
# from django.contrib.contenttypes.admin import GenericTabularInline


# class PregradosDocenteInline(GenericTabularInline):
#     model = PregradosDocente
#     extra = 1


# class PostgradosDocenteInline(GenericTabularInline):
#     model = PostgradosDocente
#     extra = 1


class EmailInline(admin.StackedInline):
    model = Email
    extra = 1


class TelefonoInline(admin.StackedInline):
    model = Telefono
    extra = 1


class DocentesInline(admin.ModelAdmin):
    inlines = [TelefonoInline, EmailInline]

    # inlines = [
    #     TelefonoInline, EmailInline, PregradosDocenteInline,
    #     PostgradosDocenteInline]
    search_fields = ('cedula', )


admin.site.register(Docentes, DocentesInline)
# admin.site.register(Pregrados)
# admin.site.register(Postgrados)
