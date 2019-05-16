from django.contrib import admin
from carrera.models import UnidadCurricular, Malla, Subestructura,\
    SubSubEstructura, MallaUCE


class MallaUCEAdmin(admin.ModelAdmin):
    raw_id_fields = ('unidad_credito', 'sub_sub_estructura')
    list_display = ('unidad_credito', 'malla', 'sub_sub_estructura')
    list_filter = ('malla', 'sub_sub_estructura')


class SubSubEstructuraInline(admin.StackedInline):
    model = SubSubEstructura
    extra = 0


class SubestructuraAdmin(admin.ModelAdmin):
    inlines = [SubSubEstructuraInline, ]


class SubEstructuraInline(admin.StackedInline):
    model = Subestructura
    extra = 0


class MallaAdmin(admin.ModelAdmin):
    inlines = [SubEstructuraInline, ]


class UnidadCurricularAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre',)

admin.site.register(UnidadCurricular, UnidadCurricularAdmin)
admin.site.register(Malla, MallaAdmin)
admin.site.register(Subestructura, SubestructuraAdmin)
admin.site.register(SubSubEstructura)
admin.site.register(MallaUCE, MallaUCEAdmin)
