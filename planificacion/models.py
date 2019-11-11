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
    periodo = models.ForeignKey(
        Periodo, on_delete=models.CASCADE,
        related_name="malla_periodo_p")
    trimestre = models.ForeignKey(
        SubSubEstructura, null=True, on_delete=models.SET_NULL)
    secciones = models.IntegerField(u'secciones')

    @property
    def trayecto(self):
        return self.trimestre.subestructura.nombre

    def __str__(self):
        return self.trimestre.codigo


class Seccion(models.Model):
    codigo = models.CharField(u'Codigo', max_length=20, unique=True)
    nombre = models.CharField(u'Nombre', max_length=200)
    turno = models.CharField(
        u'Turno', max_length=20, choices=TURNO_CHOICES, null=True, blank=False,
        default='Diurno')
    multiplicador = models.FloatField(
        "Multiplicador", default=0, null=True, blank=True)
    grupos = models.BooleanField("Grupos", default=False)
    periodo = models.ForeignKey(
        MallaUCEPeriodo, on_delete=models.CASCADE,
        related_name="seccion_malla_periodo")

    def __str__(self):
        return self.codigo


class SeccionPeriodo(models.Model):
    seccion = models.ForeignKey(Seccion, on_delete=models.CASCADE)
    docentes = models.ForeignKey(
        Docentes, on_delete=models.SET_NULL, null=True, blank=True,
        related_name='seccion_periodo_docente')
    unidad_curricular = models.ForeignKey(
        UnidadCurricular, on_delete=models.SET_NULL, null=True)
    horas_teoricas = models.FloatField(
        "Horas Teoricas", default=0, null=True, blank=True)
    horas_practicas = models.FloatField(
        "Horas Practicas", default=0, null=True, blank=True)

    def __str__(self):
        return self.seccion.codigo

    @property
    def horas_semanales(self):
        return self.horas_teoricas + self.horas_practicas
