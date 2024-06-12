from django.contrib.auth.models import User
from django.db import models


class Paciente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nutricionista = models.ForeignKey(User, on_delete=models.CASCADE, related_name='nutricionista')
    peso = models.FloatField()
    altura = models.FloatField()
