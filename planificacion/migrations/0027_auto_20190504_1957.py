# Generated by Django 2.2 on 2019-05-04 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planificacion', '0026_periodo_malla_uce'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='periodo',
            name='malla_uce',
        ),
        migrations.AddField(
            model_name='periodo',
            name='sub_sub_estructura',
            field=models.ManyToManyField(blank=True, to='planificacion.SubSubEstructura'),
        ),
    ]
