# Generated by Django 2.2 on 2019-12-29 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('docentes', '0004_auto_20191111_0320'),
        ('planificacion', '0045_auto_20191111_0301'),
    ]

    operations = [
        migrations.AddField(
            model_name='seccionperiodo',
            name='suplente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='seccion_periodo_docente_suplente', to='docentes.Docentes'),
        ),
    ]
