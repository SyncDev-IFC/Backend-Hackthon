from django.db import models
from django.utils import timezone

from core.models import Trimestre, Turma

class Conselho(models.Model):
    trimestre = models.ForeignKey(Trimestre, on_delete=models.CASCADE, related_name='conselho')
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE, related_name='conselho')
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_fim = models.DateTimeField(null=True, blank=True)
    ativo = models.BooleanField(default=False)

    def __str__(self):
        status  = "Ativado" if self.ativo else "Desativado"
        return f"{self.turma.nome} - {self.trimestre.nome} ({status})"
    
    def ativar_conselho(self):
        self.ativo = True
        self.data_inicio = timezone.now()
        self.save()

    def desativar_conselho(self):
        self.ativo = False
        self.data_fim = timezone.now()
        self.save()