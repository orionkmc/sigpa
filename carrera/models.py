from django.db import models


class UnidadCurricular(models.Model):
    nombre = models.CharField(u'Nombre', max_length=200)
    uni_credi = models.CharField(u'Unidad de Credito', max_length=10)
    codigo = models.CharField(u'codigo', max_length=10, unique=True)
    descripcion = models.TextField(u'Descripcion', null=True, blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Materia'
        verbose_name_plural = 'Materias'


class Malla(models.Model):
    cod = models.CharField(u'Nombre', max_length=100)
    fecha = models.DateField("Fecha", null=True, blank=True, auto_now=True)

    def __str__(self):
        return self.cod


class Subestructura(models.Model):
    codigo = models.CharField(u'Codigo', max_length=20, unique=True)
    nombre = models.CharField(u'Nombre', max_length=200)
    subperiodos = models.IntegerField(u'Subperiodos')
    malla = models.ForeignKey(
        Malla, null=True, on_delete=models.SET_NULL,
        related_name="malla_subestructura")

    def __str__(self):
        return self.codigo


class SubSubEstructura(models.Model):
    codigo = models.CharField(u'Codigo', max_length=20, unique=True)
    nombre = models.CharField(u'Nombre', max_length=200)
    duracion = models.IntegerField(u'Duración')
    subestructura = models.ForeignKey(
        Subestructura, null=True, on_delete=models.SET_NULL)
    parentId = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.codigo


class MallaUCE(models.Model):
    horas_teoricas = models.FloatField(
        "Horas Teoricas", default=0, null=True, blank=True)
    horas_practicas = models.FloatField(
        "Horas Practicas", default=0, null=True, blank=True)
    malla = models.ForeignKey(
        Malla, null=True, on_delete=models.SET_NULL)
    sub_sub_estructura = models.ForeignKey(
        SubSubEstructura, null=True, on_delete=models.SET_NULL,
        related_name="malla_uce_sub_sub_estructura")
    unidad_credito = models.ForeignKey(
        UnidadCurricular, null=True, on_delete=models.SET_NULL,
        related_name="malla_unidad_credito")
    laboratorio = models.BooleanField(default=False)

    def __str__(self):
        return self.unidad_credito.nombre

    @property
    def horas_total(self):
        return self.horas_teoricas + self.horas_practicas
