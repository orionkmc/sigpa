# Generated by Django 2.2 on 2019-04-30 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planificacion', '0009_mallauce'),
    ]

    operations = [
        migrations.AddField(
            model_name='mallauce',
            name='laboratorio',
            field=models.BooleanField(default=False),
        ),
    ]