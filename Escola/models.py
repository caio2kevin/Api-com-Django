from django.db import models


class Estudante(models.Model):
    nome = models.CharField(max_length=100, blank=False)
    email = models.EmailField(blank=False, unique=True)
    cpf = models.CharField(max_length=11, unique=True)
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length=14, blank=True, null=True)

    def __str__(self):
        return self.nome


class Curso(models.Model):
    NIVEL = (
        ('B', 'Básico'),
        ('I', 'Intermediário'),
        ('A', 'Avançado'),
    )

    codigo = models.CharField(max_length=10, unique=True)
    descricao = models.CharField(max_length=100, blank=False)
    nivel = models.CharField(max_length=1, choices=NIVEL, blank=False, default='B')

    def __str__(self):
        return self.codigo
