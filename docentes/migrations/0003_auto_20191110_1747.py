# Generated by Django 2.2 on 2019-11-10 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docentes', '0002_auto_20191110_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docentes',
            name='cedula',
            field=models.PositiveIntegerField(blank=True, null=True, unique=True, verbose_name='cedula'),
        ),
        migrations.AlterField(
            model_name='docentes',
            name='direccion',
            field=models.TextField(blank=True, null=True, verbose_name='Dirección'),
        ),
    ]