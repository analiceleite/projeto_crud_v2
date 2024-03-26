from django.db import models

class Cliente(models.Model):
  nome = models.CharField(max_length=100)
  endereco = models.TextField()
  cpf = models.CharField(max_length=14, unique=True)
  data_nascimento = models.DateField()

  def __str__(self):
      return self.nome