from django.db import models

# Create your models here.

class Dados_Funcionario(models.Model):
    Nome = models.CharField(max_length=50)
    Cpf = models.CharField(max_length=14)
    Idade = models.IntegerField()
    Data_de_Nascimento = models.DateField()
    Telefone = models.CharField(max_length=20)
    Email = models.EmailField(max_length=60)

    def __str__(self):
        return self.Nome
