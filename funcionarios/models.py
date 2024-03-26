from django.db import models

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    edv = models.CharField(max_length=8, unique=True)
    cargo = models.CharField(max_length=100)
    setor = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    horario_entrada = models.TimeField()
    horario_saida = models.TimeField()
    data_admissao = models.DateField()
    
    def __str__(self):
        return self.nome