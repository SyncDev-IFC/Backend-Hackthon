from django.db import models

from core.models import Conselho, Aluno

class Anotacao(models.Model):
    class Tipo(models.TextChoices):
        FAMILIAESCOLA = 1, 'Reunião Família-Escola'
        GRUPOESTUDOS = 2, 'Participação em Grupo de Estudos'
        SISAE = 3, 'Participação em SiSAE'
        REGENTE  = 4, 'Reunião com Regente'
        CORDENACAO = 5, 'Reunião com Coordenação de Curso'

    acoes = models.CharField(max_length=2, choices=Tipo.choices,) 
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    conselho = models.ForeignKey(Conselho, on_delete=models.CASCADE, related_name='anotacoes', null=True, blank=True, default=None)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name='anotacoes', null=True, blank=True, default=None)


    def __str__(self):
        return self.titulo