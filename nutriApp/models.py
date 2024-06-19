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

    def __str__(self):
        return self.nome_completo

class MedidaAntropometrica(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='medidas')
    data_medicao = models.DateField(verbose_name='Data da Medição', blank=False)
    altura = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Altura (cm)', blank=False)
    peso = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Peso (kg)', blank=False)
    circunferencia_abdominal = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Circunferência Abdominal (cm)', blank=True, null=True)
    circunferencia_quadril = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Circunferência do Quadril (cm)', blank=True, null=True)
    imc = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='Índice de Massa Corporal (IMC)', blank=True, null=True)

    def __str__(self):
        return f'Medida de {self.paciente.nome_completo} em {self.data_medicao}'