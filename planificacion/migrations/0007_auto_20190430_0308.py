# Generated by Django 2.2 on 2019-04-30 03:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('planificacion', '0006_auto_20190430_0255'),
    ]

    operations = [
        migrations.RenameField(
            model_name='periodo',
            old_name='periodo',
            new_name='estructura',
        ),
        migrations.CreateModel(
            name='Malla',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod', models.CharField(max_length=100, verbose_name='Trayecto y Trimestre')),
                ('fecha', models.DateField(auto_now=True, null=True, verbose_name='fecha')),
                ('estructura', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='planificacion.Estructura')),
            ],
        ),
    ]