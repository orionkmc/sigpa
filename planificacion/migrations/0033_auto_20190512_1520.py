# Generated by Django 2.2 on 2019-05-12 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carrera', '0008_auto_20190512_1520'),
        ('planificacion', '0032_mallauceperiodo_malla_uce'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mallauceperiodo',
            name='malla_uce',
        ),
        migrations.AddField(
            model_name='mallauceperiodo',
            name='subsubestructura',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='carrera.SubSubEstructura'),
        ),
    ]