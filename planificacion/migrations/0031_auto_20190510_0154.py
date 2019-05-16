# Generated by Django 2.2 on 2019-05-10 01:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planificacion', '0030_auto_20190504_2107'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='malla',
            name='estructura',
        ),
        migrations.RemoveField(
            model_name='mallauce',
            name='malla',
        ),
        migrations.RemoveField(
            model_name='mallauce',
            name='sub_sub_estructura',
        ),
        migrations.RemoveField(
            model_name='mallauce',
            name='unidad_credito',
        ),
        migrations.RemoveField(
            model_name='subestructura',
            name='estructura',
        ),
        migrations.RemoveField(
            model_name='subsubestructura',
            name='subestructura',
        ),
        migrations.RemoveField(
            model_name='unidadcurricular',
            name='eje',
        ),
        migrations.RemoveField(
            model_name='mallauceperiodo',
            name='malla_uce',
        ),
        migrations.RemoveField(
            model_name='seccion',
            name='sub_sub_estructura',
        ),
        migrations.DeleteModel(
            name='Eje',
        ),
        migrations.DeleteModel(
            name='Estructura',
        ),
        migrations.DeleteModel(
            name='Malla',
        ),
        migrations.DeleteModel(
            name='MallaUCE',
        ),
        migrations.DeleteModel(
            name='Subestructura',
        ),
        migrations.DeleteModel(
            name='SubSubEstructura',
        ),
        migrations.DeleteModel(
            name='UnidadCurricular',
        ),
    ]