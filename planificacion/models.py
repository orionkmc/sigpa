from django.db import models
from carrera.models import SubSubEstructura, UnidadCurricular
from docentes.models import Docentes

TURNO_CHOICES = (
    ('diurno', 'Diurno'),
    ('nocturno', 'Nocturno'),
)


class Periodo(models.Model):
    codigo = models.CharField(u'Codigo', max_length=20, unique=True)
    nombre = models.CharField(u'Nombre', max_length=200)
    fecha_inicio = models.DateField("Fecha Inicio")
    fecha_fin = models.DateField("Fecha Fin",)

    def __str__(self):
        return self.codigo

    class Meta:
        ordering = ('-pk', )


class MallaUCEPeriodo(models.Model):
    periodo = models.ForeignKey(Periodo, null=True, on_delete=models.SET_NULL)
    trimestre = models.ForeignKey(
        SubSubEstructura, null=True, on_delete=models.SET_NULL)
    secciones = models.IntegerField(u'secciones')

    @property
    def trayecto(self):
        return self.trimestre.subestructura.nombre

    def __str__(self):
        return self.trimestre.codigo


class Seccion(models.Model):
    codigo = models.CharField(u'Codigo', max_length=20)
    nombre = models.CharField(u'Nombre', max_length=200)
    turno = models.CharField(
        u'Turno', max_length=20, choices=TURNO_CHOICES, null=True, blank=False,
        default='Diurno')
    multiplicador = models.FloatField(
        "Multiplicador", default=0, null=True, blank=True)
    grupos = models.BooleanField("Grupos", default=False)
    periodo = models.ForeignKey(
        MallaUCEPeriodo, null=True, on_delete=models.SET_NULL,
        related_name="seccion_malla_periodo")

    def __str__(self):
        return self.nombre


class SeccionPeriodo(models.Model):
    seccion = models.ForeignKey(
        Seccion, on_delete=models.SET_NULL, null=True)
    docentes = models.ForeignKey(
        Docentes, on_delete=models.SET_NULL, null=True)
    unidad_curricular = models.ForeignKey(
        UnidadCurricular, on_delete=models.SET_NULL, null=True)
