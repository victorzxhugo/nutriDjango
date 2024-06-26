# Generated by Django 5.0.6 on 2024-06-26 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nutriApp', '0008_alter_paciente_genero'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='imc',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='paciente',
            name='percentual_massa_gorda',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='paciente',
            name='percentual_massa_muscular',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='massa_gorda',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='massa_muscular',
            field=models.FloatField(blank=True, default=0),
        ),
    ]
