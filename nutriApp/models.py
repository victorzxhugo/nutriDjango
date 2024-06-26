from django.contrib.auth.models import User
from django.db import models
from django.core.validators import RegexValidator

class Paciente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nutricionista = models.ForeignKey(User, on_delete=models.CASCADE, related_name='paciente_nutricionista')
    nome_completo = models.CharField(max_length=255, verbose_name='Nome Completo', blank=False)
    genero = models.CharField(max_length=20, choices=[('Masculino', 'Masculino'), ('Feminino', 'Feminino'), ('Outro', 'Outro')], default='Masculino')
    data_nascimento = models.DateField(verbose_name='Data de Nascimento', blank=False)
    ocupacao = models.CharField(max_length=150, blank=True)
    cep = models.CharField(max_length=9, verbose_name='CEP', blank=True, validators=[RegexValidator(regex=r'^\d{5}-\d{3}$')])
    celular = models.CharField(max_length=15, validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$')], verbose_name='Celular', blank=True)
    
    peso = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Peso (kg)', blank=False, default=0)
    altura = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Altura (cm)', blank=False, default=0)
    dobra_cutanea_iliocristal = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Dobra Cutânea Iliocristal', blank=False, default=0)
    dobra_cutanea_supraespinhal = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Dobra Cutânea Supraespinhal', blank=False, default=0)
    dobra_cutanea_abdominal = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Dobra Cutânea Abdominal', blank=False, default=0)
    dobra_cutanea_axilar_media = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Dobra Cutânea Axilar Média', blank=False, default=0)
    dobra_cutanea_coxa = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Dobra Cutânea Coxa', blank=False, default=0)
    dobra_cutanea_peitoral = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Dobra Cutânea Peitoral', blank=False, default=0)
    dobra_cutanea_subescapular = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Dobra Cutânea Subescapular', blank=False, default=0)
    dobra_cutanea_suprailiaca = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Dobra Cutânea Supra-ilíaca', blank=False, default=0)
    dobra_cutanea_tricipital = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Dobra Cutânea Tricipital', blank=False, default=0)
    perimetro_cintura = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Perímetro da Cintura', blank=False, default=0)
    perimetro_quadril = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Perímetro do Quadril', blank=False, default=0)
    colesterol_hdl = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Colesterol HDL', blank=False, default=0)
    colesterol_ldl = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Colesterol LDL', blank=False, default=0)
    colesterol_total = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Colesterol Total', blank=False, default=0)
    pressao_arterial_diastolica = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Pressão Arterial Diastólica', blank=False, default=0)
    pressao_arterial_sistolica = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Pressão Arterial Sistólica', blank=False, default=0)
    triglicerideos = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Triglicerídeos', blank=False, default=0)
    massa_gorda = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Massa Gorda (kg)', blank=False, default=0)
    massa_muscular = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Massa Muscular (kg)', blank=False, default=0)
    porcentagem_massa_gorda = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Porcentagem de Massa Gorda (%)', blank=False, default=0)
    porcentagem_massa_muscular = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Porcentagem de Massa Muscular (%)', blank=False, default=0)
    
    objetivo_consulta = models.TextField(verbose_name='Objetivo da Consulta', blank=True)
    historico_alimentar = models.TextField(verbose_name='Histórico Alimentar', blank=True)
    alergias = models.TextField(verbose_name='Alergias', blank=True)
    rotina_de_alimentacao = models.TextField(verbose_name='Rotina de Alimentação', blank=True)
    rotina_de_atividade_fisica = models.TextField(verbose_name='Rotina de Atividade Física', blank=True)
    preferencias_e_restricoes = models.TextField(verbose_name='Preferências e Restrições', blank=True)

    data_medicao = models.DateField(verbose_name='Data da Medição', blank=False, null=True)
    historico = models.TextField(verbose_name='Histórico', blank=True)

    def __str__(self):
        return self.nome_completo