# Generated by Django 2.2 on 2019-11-10 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('docentes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='docentes',
            options={'ordering': ('nombre',), 'verbose_name': 'Docente', 'verbose_name_plural': 'Docentes'},
        ),
    ]