from django.contrib import admin
from planificacion.models import Periodo, Seccion, MallaUCEPeriodo,\
    SeccionPeriodo


class MallaUCEPeriodoInline(admin.StackedInline):
    model = MallaUCEPeriodo
    extra = 0


# class SubSubEstructuraInline(admin.StackedInline):
#     model = SubSubEstructura
#     extra = 0


# class MallaUCEInline(admin.StackedInline):
#     model = MallaUCE
#     extra = 0
#     raw_id_fields = ('unidad_credito', )


# class SeccionInline(admin.StackedInline):
#     model = Seccion
#     extra = 0


# class EstructuraAdmin(admin.ModelAdmin):
#     inlines = [PeriodoInline, ]


# class SubestructuraAdmin(admin.ModelAdmin):
#     inlines = [SubSubEstructuraInline, ]


# class MallaAdmin(admin.ModelAdmin):
#     inlines = [MallaUCEInline, ]


class SeccionesAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'periodo')


class PeriodoAdmin(admin.ModelAdmin):
    inlines = [MallaUCEPeriodoInline, ]
    # filter_horizontal = ('sub_sub_estructura', )
    # raw_id_fields = ('malla_uce', )
    # inlines = [SeccionInline, ]
    pass


class MallaUCEPeriodoAdmin(admin.ModelAdmin):
    list_display = (
        'periodo', 'secciones', 'trayecto', 'trimestre')
    list_filter = ('periodo', )


class SeccionPeriodoAdmin(admin.ModelAdmin):
    list_filter = ('seccion', )
    list_display = ('seccion', 'docentes', 'unidad_curricular')


# admin.site.register(Estructura, EstructuraAdmin)
# admin.site.register(Subestructura, SubestructuraAdmin)
# admin.site.register(SubSubEstructura)
# admin.site.register(Eje)
# admin.site.register(UnidadCurricular, UnidadCurricularAdmin)
# admin.site.register(Malla, MallaAdmin)
# admin.site.register(MallaUCE, MallaUCEAdmin)
admin.site.register(SeccionPeriodo, SeccionPeriodoAdmin)
admin.site.register(Periodo, PeriodoAdmin)
admin.site.register(Seccion, SeccionesAdmin)
admin.site.register(MallaUCEPeriodo, MallaUCEPeriodoAdmin)
