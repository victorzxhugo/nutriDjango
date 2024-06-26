# Generated by Django 5.0.6 on 2024-06-26 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nutriApp', '0009_paciente_imc_paciente_percentual_massa_gorda_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paciente',
            name='percentual_massa_gorda',
        ),
        migrations.RemoveField(
            model_name='paciente',
            name='percentual_massa_muscular',
        ),
        migrations.AlterField(
            model_name='paciente',
            name='massa_gorda',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, verbose_name='Massa Gorda (kg)'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='massa_muscular',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, verbose_name='Massa Muscular (kg)'),
        ),
    ]