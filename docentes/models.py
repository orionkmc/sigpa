from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

DEDICAION = (
    ('EXC', 'Exclusiva'),
    ('TC', 'Tiempo Completo'),
    ('MT', 'Medio Tiempo'),
    ('TCV', 'Tiempo Convencional'),
)

Estatus = (
    ('Ordinario', 'Ordinario'),
    ('Contratado', 'Contratado'),
)

CATEGORIA = (
    ('Titular', 'Titular'),
    ('Asociado', 'Asociado'),
    ('Agregado', 'Agregado'),
    ('Asistente', 'Asistente'),
    ('Instructor', 'Instructor'),
)


class Telefono(models.Model):
    id = models.AutoField(primary_key=True)
    telefono = models.CharField(u'Telefono', max_length=20, unique=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    fecha_de_creacion = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Telefono'
        verbose_name_plural = 'Telefonos'


class Email(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(u'Email', max_length=50, unique=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    fecha_de_creacion = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Email'
        verbose_name_plural = 'Emails'


class Pregrados(models.Model):
    nombre = models.CharField(u'Pregrado', max_length=50)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Pregrado'
        verbose_name_plural = 'Pregrados'


class Postgrados(models.Model):
    nombre = models.CharField(u'Pregrado', max_length=50)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Postgrado'
        verbose_name_plural = 'Postgrados'


class PregradosDocente(models.Model):
    id = models.AutoField(primary_key=True)
    pregrado = models.ForeignKey(
        Pregrados, null=True, on_delete=models.SET_NULL)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    fecha_de_creacion = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Pregrado'
        verbose_name_plural = 'Pregrados'


class PostgradosDocente(models.Model):
    id = models.AutoField(primary_key=True)
    pregrado = models.ForeignKey(
        Pregrados, null=True, on_delete=models.SET_NULL)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    fecha_de_creacion = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Postgrado'
        verbose_name_plural = 'Postgrados'


class Docentes(models.Model):
    cedula = models.PositiveIntegerField('cedula', unique=True)
    nombre = models.CharField(u'Nombre', max_length=50)
    apellido = models.CharField(u'Apellido', max_length=50)
    direccion = models.TextField(u'Dirección')
    dedicacion = models.CharField(
        u'Dedicacion', max_length=5, choices=DEDICAION, default='TC')
    categoria = models.CharField(
        u'Categoria', max_length=10, choices=CATEGORIA, default='Instructor')
    status = models.CharField(
        u'Estatus', max_length=15, choices=Estatus, default='Contratado')

    class Meta:
        verbose_name = 'Docente'
        verbose_name_plural = 'Docentes'

    def __str__(self):
        return self.nombre
