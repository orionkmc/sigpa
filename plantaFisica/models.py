from django.db import models


class Edificio(models.Model):
    codigo = models.CharField(u'Codigo/Nombre', max_length=50, unique=True)

    def __str__(self):
        return self.codigo

    class Meta:
        verbose_name = 'Edificio'
        verbose_name_plural = 'Edificios'
        ordering = ('codigo', )


class Piso(models.Model):
    codigo = models.CharField(u'Codigo/Nombre', max_length=50)
    edificio = models.ForeignKey(Edificio, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.edificio) + ' ' + str(self.codigo)

    class Meta:
        verbose_name = 'Piso'
        verbose_name_plural = 'Pisos'
        ordering = ('edificio', )


class Salon(models.Model):
    codigo = models.CharField(u'Codigo/Nombre', max_length=50)
    piso = models.ForeignKey(Piso, on_delete=models.CASCADE)

    def __str__(self):
        return self.codigo

    class Meta:
        verbose_name = 'Salon'
        verbose_name_plural = 'Salones'
