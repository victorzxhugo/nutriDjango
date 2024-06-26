# Generated by Django 5.0.6 on 2024-06-26 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nutriApp', '0004_paciente_historico'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='altura',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, verbose_name='Altura (cm)'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='colesterol_hdl',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, verbose_name='Colesterol HDL'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='colesterol_ldl',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, verbose_name='Colesterol LDL'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='colesterol_total',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, verbose_name='Colesterol Total'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='data_medicao',
            field=models.DateField(blank=True, null=True, verbose_name='Data da Medição'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='dobra_cutanea_abdominal',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, verbose_name='Dobra Cutânea Abdominal'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='dobra_cutanea_axilar_media',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, verbose_name='Dobra Cutânea Axilar Média'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='dobra_cutanea_coxa',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, verbose_name='Dobra Cutânea Coxa'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='dobra_cutanea_iliocristal',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, verbose_name='Dobra Cutânea Iliocristal'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='dobra_cutanea_peitoral',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, verbose_name='Dobra Cutânea Peitoral'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='dobra_cutanea_subescapular',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, verbose_name='Dobra Cutânea Subescapular'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='dobra_cutanea_supraespinhal',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, verbose_name='Dobra Cutânea Supraespinhal'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='dobra_cutanea_suprailiaca',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, verbose_name='Dobra Cutânea Supra-ilíaca'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='dobra_cutanea_tricipital',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, verbose_name='Dobra Cutânea Tricipital'),
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
        migrations.AlterField(
            model_name='paciente',
            name='perimetro_cintura',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, verbose_name='Perímetro da Cintura'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='perimetro_quadril',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, verbose_name='Perímetro do Quadril'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='peso',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, verbose_name='Peso (kg)'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='porcentagem_massa_gorda',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, verbose_name='Porcentagem de Massa Gorda (%)'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='porcentagem_massa_muscular',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, verbose_name='Porcentagem de Massa Muscular (%)'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='pressao_arterial_diastolica',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, verbose_name='Pressão Arterial Diastólica'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='pressao_arterial_sistolica',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, verbose_name='Pressão Arterial Sistólica'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='triglicerideos',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, verbose_name='Triglicerídeos'),
        ),
    ]
