# Generated by Django 2.2 on 2020-01-19 21:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plantaFisica', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salon',
            name='piso',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='plantaFisica.Piso'),
        ),
    ]