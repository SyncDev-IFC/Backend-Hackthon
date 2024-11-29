from django.db import models

from core.models import Turma, Aluno, Trimestre

class Observacao(models.Model):
    conteudo = models.TextField()
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name='observacoes', null=True, blank=True)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE, related_name='observacoes', null=True, blank=True)
    trimestre = models.ForeignKey(Trimestre, on_delete=models.CASCADE, related_name='observacoes', null=True, blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)  

    
    def __str__(self):
        return f"{self.trimestre} ({self.get_associado()})"
    
    def get_associado(self):
        if self.turma:
            return f"Turma: {self.aluno.turma.nome}"
        elif self.aluno:
            return f"Aluno: {self.aluno.nome}"
        return "Não associado"
    
class Meta:
    ordering = ["-data_criacao"]  
    