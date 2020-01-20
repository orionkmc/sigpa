from django.db import models
from carrera.models import SubSubEstructura, UnidadCurricular
from docentes.models import Docentes
from plantaFisica.models import Salon

TURNO_CHOICES = (
    ('diurno', 'Diurno'),
    ('nocturno', 'Nocturno'),
)

DIA_CHOICES = (
    ('Lunes', 'Lunes'),
    ('Martes', 'Martes'),
    ('Miercoles', 'Miercoles'),
    ('Jueves', 'Jueves'),
    ('Viernes', 'Viernes'),
    ('Sabado', 'Sabado'),
    ('Domingo', 'Domingo'),
)

HORA_CHOICES = (
    ('1', '07:00 a 07:45'),
    ('2', '07:45 a 08:30'),
    ('3', '08:40 a 09:25'),
    ('4', '09:25 a 10:10'),
    ('5', '10:20 a 11:05'),
    ('6', '11:05 a 11:50'),
    ('7', '11:50 a 12:45'),
    ('8', '12:45 a 01:30'),
    ('9', '01:30 a 02:25'),
    ('10', '02:25 a 03:10'),
    ('11', '03:10 a 03:55'),
    ('12', '04:05 a 04:50'),
    ('13', '04:50 a 05:35'),
    ('14', '05:45 a 06:30'),
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
    codigo = models.CharField(u'Codigo', max_length=50, unique=True)
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

    class Meta:
        ordering = ('codigo', )


class SeccionPeriodo(models.Model):
    seccion = models.ForeignKey(Seccion, on_delete=models.CASCADE)
    docentes = models.ForeignKey(
        Docentes, on_delete=models.SET_NULL, null=True, blank=True,
        related_name='seccion_periodo_docente')
    suplente = models.ForeignKey(
        Docentes, on_delete=models.SET_NULL, null=True, blank=True,
        related_name='seccion_periodo_docente_suplente')
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


class Horarios(models.Model):
    seccion_periodo = models.ForeignKey(
        SeccionPeriodo, on_delete=models.CASCADE,
        related_name='horarios_seccion_periodo')
    salon = models.ForeignKey(
        Salon, on_delete=models.CASCADE, null=True, blank=True)
    dia = models.CharField(
        u'Dia', max_length=20, choices=DIA_CHOICES, null=True, blank=True)
    desde = models.CharField(
        u'Hora Desde', max_length=20, choices=HORA_CHOICES, null=True,
        blank=True)
    hasta = models.CharField(
        u'Hora Hasta', max_length=20, choices=HORA_CHOICES, null=True,
        blank=True)

    class Meta:
        ordering = ('desde', )
        verbose_name = 'Horario'
        verbose_name_plural = 'Horarios'
