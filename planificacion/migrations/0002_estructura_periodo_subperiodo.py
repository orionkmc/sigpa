# Generated by Django 2.2 on 2019-04-30 01:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('planificacion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Periodo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, verbose_name='Nombre')),
            ],
        ),
        migrations.CreateModel(
            name='Subperiodo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=20, verbose_name='Codigo')),
                ('nombre', models.CharField(max_length=200, verbose_name='Nombre')),
                ('duracion', models.IntegerField(verbose_name='Duración')),
                ('periodo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='planificacion.Periodo')),
            ],
        ),
    ]
