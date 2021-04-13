from django.db import models


class Curso(models.Model):
    nome = models.CharField('Curso', max_length=200)
    ano = models.IntegerField('Conclusão')

    def __str__(self):
        return self.nome
