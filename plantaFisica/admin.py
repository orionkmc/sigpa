from django.contrib import admin
from plantaFisica.models import Edificio, Piso, Salon


class PisoAdmin(admin.ModelAdmin):
    list_display = ('edificio', 'codigo')


class SalonAdmin(admin.ModelAdmin):
    list_display = ('piso__edificio__codigo', 'piso__codigo', 'codigo')

    def piso__edificio__codigo(self, obj):
        if obj.piso is not None:
            return obj.piso.edificio.codigo
        return '-'
    piso__edificio__codigo.short_description = 'Edificio'
    piso__edificio__codigo.admin_order_field = 'piso__edificio__codigo'

    def piso__codigo(self, obj):
        if obj.piso is not None:
            return obj.piso.codigo
        return '-'
    piso__codigo.short_description = 'Piso'
    piso__codigo.admin_order_field = 'piso__codigo'


admin.site.register(Edificio)
admin.site.register(Piso, PisoAdmin)
admin.site.register(Salon, SalonAdmin)
