# Generated by Django 2.2 on 2020-01-19 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planificacion', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='horarios',
            options={'verbose_name': 'Horario', 'verbose_name_plural': 'Horarios'},
        ),
        migrations.RemoveField(
            model_name='horarios',
            name='hora',
        ),
        migrations.AddField(
            model_name='horarios',
            name='desde',
            field=models.CharField(blank=True, choices=[('1', '07:00 a 07:45'), ('2', '07:45 a 08:30'), ('3', '08:40 a 09:25'), ('4', '09:25 a 10:10'), ('5', '10:20 a 11:05'), ('6', '11:05 a 11:50'), ('7', '11:50 a 12:45'), ('8', '12:45 a 01:30'), ('9', '01:30 a 02:25'), ('10', '02:25 a 03:10'), ('11', '03:10 a 03:55'), ('12', '04:05 a 04:50'), ('13', '04:50 a 05:35'), ('14', '05:45 a 06:30')], max_length=20, null=True, verbose_name='Hora Desde'),
        ),
        migrations.AddField(
            model_name='horarios',
            name='hasta',
            field=models.CharField(blank=True, choices=[('1', '07:00 a 07:45'), ('2', '07:45 a 08:30'), ('3', '08:40 a 09:25'), ('4', '09:25 a 10:10'), ('5', '10:20 a 11:05'), ('6', '11:05 a 11:50'), ('7', '11:50 a 12:45'), ('8', '12:45 a 01:30'), ('9', '01:30 a 02:25'), ('10', '02:25 a 03:10'), ('11', '03:10 a 03:55'), ('12', '04:05 a 04:50'), ('13', '04:50 a 05:35'), ('14', '05:45 a 06:30')], max_length=20, null=True, verbose_name='Hora Hasta'),
        ),
    ]
