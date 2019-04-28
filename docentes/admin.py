from django.contrib import admin
from docentes.models import Docentes, Pregrados, Postgrados, Telefono, Email,\
    PregradosDocente, PostgradosDocente
from django.contrib.contenttypes.admin import GenericTabularInline


class PregradosDocenteInline(GenericTabularInline):
    model = PregradosDocente
    extra = 1


class PostgradosDocenteInline(GenericTabularInline):
    model = PostgradosDocente
    extra = 1


class EmailInline(GenericTabularInline):
    model = Email
    extra = 1


class TelefonoInline(GenericTabularInline):
    model = Telefono
    extra = 1


class DocentesInline(admin.ModelAdmin):
    inlines = [
        TelefonoInline, EmailInline, PregradosDocenteInline,
        PostgradosDocenteInline]


admin.site.register(Docentes, DocentesInline)
admin.site.register(Pregrados)
admin.site.register(Postgrados)
