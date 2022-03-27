from venv import create
from django.db import models
from django.forms import CharField

class Post(models.Model):
    titulo = models.CharField(max_length=100, blank=False) 
    texto = models.TextField(blank=False)
    
    def __str__ (self):
        return self.titulo

""" Class para realizar o cadastro do usuário """
class Cadastro(models.Model):
    nome = models.CharField(max_length=50)
    idade = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    senha = models.CharField(max_length=50)
    telefone = models.CharField(max_length=15, verbose_name="Endereço")
    endereco = models.CharField(max_length=50)

    def __str__ (self):
        return "{ } ( { } )".format(self.nome, self.descricao)

class Tabela(models.Model):
    informacao = models.CharField(max_length=100)

    def __str__ (self):
        return "{ } ( { } )".format(self.nome, self.descricao)





