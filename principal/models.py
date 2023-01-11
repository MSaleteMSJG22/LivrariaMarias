from distutils.command.upload import upload
from unittest.util import _MAX_LENGTH
from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=200)

    def __str__ (self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    valor = models.DecimalField('Preco do Produto', max_digits=8, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to = 'imag/', blank=True, null=True, max_length=150)

    def __str__ (self):
        return self.nome