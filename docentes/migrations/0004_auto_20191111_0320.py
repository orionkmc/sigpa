# Generated by Django 2.2 on 2019-11-11 03:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('docentes', '0003_auto_20191110_1747'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Postgrados',
        ),
        migrations.RemoveField(
            model_name='pregradosdocente',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='pregradosdocente',
            name='pregrado',
        ),
        migrations.RemoveField(
            model_name='email',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='email',
            name='object_id',
        ),
        migrations.RemoveField(
            model_name='telefono',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='telefono',
            name='object_id',
        ),
        migrations.AddField(
            model_name='email',
            name='docente',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='docentes.Docentes'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='telefono',
            name='docente',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='docentes.Docentes'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='PostgradosDocente',
        ),
        migrations.DeleteModel(
            name='Pregrados',
        ),
        migrations.DeleteModel(
            name='PregradosDocente',
        ),
    ]
