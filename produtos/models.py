from django.db import models

class Produto (models.Model):
    descricao = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=5,decimal_places=2)
    quantidade = models.IntegerField()
    peso = models.DecimalField(max_digits=8,decimal_places=2)
    voltagem = models.CharField(max_length=10,
        choices = (
            ('110','110'),
                ('220','220')
                )
    )
    marca = models.CharField(max_length=100)
    tipo = models.CharField (max_length=100)
    
    def __str__(self):
        return self.descricao