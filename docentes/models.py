from django.db import models

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


class Docentes(models.Model):
    cedula = models.PositiveIntegerField(
        'Cédula', unique=True, null=True, blank=True)
    nombre = models.CharField(u'Nombre', max_length=50)
    apellido = models.CharField(u'Apellido', max_length=50)
    direccion = models.TextField(u'Dirección', null=True, blank=True)
    dedicacion = models.CharField(
        u'Dedicación', max_length=5, choices=DEDICAION, default='TC')
    categoria = models.CharField(
        u'Categoría', max_length=10, choices=CATEGORIA, default='Instructor')
    status = models.CharField(
        u'Estatus', max_length=15, choices=Estatus, default='Contratado')

    class Meta:
        verbose_name = 'Docente'
        verbose_name_plural = 'Docentes'
        ordering = ('nombre', )

    def __str__(self):
        return self.nombre + ' ' + self.apellido


class Telefono(models.Model):
    id = models.AutoField(primary_key=True)
    telefono = models.CharField(u'Telefono', max_length=20, unique=True)
    docente = models.ForeignKey(
        Docentes, on_delete=models.CASCADE)
    fecha_de_creacion = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Telefono'
        verbose_name_plural = 'Telefonos'


class Email(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(u'Email', max_length=50, unique=True)
    docente = models.ForeignKey(
        Docentes, on_delete=models.CASCADE)
    fecha_de_creacion = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Email'
        verbose_name_plural = 'Emails'


# class Pregrados(models.Model):
#     nombre = models.CharField(u'Pregrado', max_length=50)

#     def __str__(self):
#         return self.nombre

#     class Meta:
#         verbose_name = 'Pregrado'
#         verbose_name_plural = 'Pregrados'


# class Postgrados(models.Model):
#     nombre = models.CharField(u'Pregrado', max_length=50)

#     def __str__(self):
#         return self.nombre

#     class Meta:
#         verbose_name = 'Postgrado'
#         verbose_name_plural = 'Postgrados'


# class PregradosDocente(models.Model):
#     nombre = models.CharField(u'Pregrado', max_length=50)
#     docente = models.ForeignKey(
#         Pregrados, null=True, on_delete=models.SET_NULL)
#     fecha_de_creacion = models.DateTimeField(
#         auto_now=False, auto_now_add=True)
#     class Meta:
#         verbose_name = 'Pregrado'
#         verbose_name_plural = 'Pregrados'


# class PostgradosDocente(models.Model):
#     id = models.AutoField(primary_key=True)
#     pregrado = models.ForeignKey(
#         Pregrados, null=True, on_delete=models.SET_NULL)
#     fecha_de_creacion = models.DateTimeField(
#         auto_now=False, auto_now_add=True)

#     class Meta:
#         verbose_name = 'Postgrado'
#         verbose_name_plural = 'Postgrados'
