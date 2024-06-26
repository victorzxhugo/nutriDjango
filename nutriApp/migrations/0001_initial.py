# Generated by Django 4.2.13 on 2024-06-20 23:53

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(max_length=255, verbose_name='Nome Completo')),
                ('genero', models.CharField(choices=[('Masculino', 'Masculino'), ('Feminino', 'Feminino'), ('Outro', 'Outro')], default='Masculino', max_length=20)),
                ('data_nascimento', models.DateField(verbose_name='Data de Nascimento')),
                ('ocupacao', models.CharField(blank=True, max_length=150)),
                ('cep', models.CharField(blank=True, max_length=9, validators=[django.core.validators.RegexValidator(regex='^\\d{5}-\\d{3}$')], verbose_name='CEP')),
                ('celular', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{9,15}$')], verbose_name='Celular')),
                ('peso', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Peso (kg)')),
                ('altura', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Altura (cm)')),
                ('dobra_cutanea_iliocristal', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Dobra Cutânea Iliocristal')),
                ('dobra_cutanea_supraespinhal', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Dobra Cutânea Supraespinhal')),
                ('dobra_cutanea_abdominal', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Dobra Cutânea Abdominal')),
                ('dobra_cutanea_axilar_media', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Dobra Cutânea Axilar Média')),
                ('dobra_cutanea_coxa', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Dobra Cutânea Coxa')),
                ('dobra_cutanea_peitoral', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Dobra Cutânea Peitoral')),
                ('dobra_cutanea_subescapular', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Dobra Cutânea Subescapular')),
                ('dobra_cutanea_suprailiaca', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Dobra Cutânea Supra-ilíaca')),
                ('dobra_cutanea_tricipital', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Dobra Cutânea Tricipital')),
                ('perimetro_cintura', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Perímetro da Cintura')),
                ('perimetro_quadril', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Perímetro do Quadril')),
                ('colesterol_hdl', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Colesterol HDL')),
                ('colesterol_ldl', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Colesterol LDL')),
                ('colesterol_total', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Colesterol Total')),
                ('pressao_arterial_diastolica', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Pressão Arterial Diastólica')),
                ('pressao_arterial_sistolica', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Pressão Arterial Sistólica')),
                ('triglicerideos', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Triglicerídeos')),
                ('massa_gorda', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Massa Gorda (kg)')),
                ('massa_muscular', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Massa Muscular (kg)')),
                ('porcentagem_massa_gorda', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Porcentagem de Massa Gorda (%)')),
                ('porcentagem_massa_muscular', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Porcentagem de Massa Muscular (%)')),
                ('objetivo_consulta', models.TextField(blank=True, verbose_name='Objetivo da Consulta')),
                ('historico_alimentar', models.TextField(blank=True, verbose_name='Histórico Alimentar')),
                ('alergias', models.TextField(blank=True, verbose_name='Alergias')),
                ('rotina_de_alimentacao', models.TextField(blank=True, verbose_name='Rotina de Alimentação')),
                ('rotina_de_atividade_fisica', models.TextField(blank=True, verbose_name='Rotina de Atividade Física')),
                ('preferencias_e_restricoes', models.TextField(blank=True, verbose_name='Preferências e Restrições')),
                ('data_medicao', models.DateField(verbose_name='Data da Medição')),
                ('nutricionista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paciente_nutricionista', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
