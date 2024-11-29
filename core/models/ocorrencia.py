from django.db import models

class Ocorrencia(models.Model):
    class Tipo(models.TextChoices):
        OCORRENCIA = 'OC', 'Ocorrência'
        OBSERVACAO = 'OB', 'Observação'
    titulo = models.CharField(max_length=100)  
    conteudo = models.TextField() 
    data_criacao = models.DateTimeField(auto_now_add=True)  
    turma = models.ForeignKey('Turma', null=True, blank=True, on_delete=models.CASCADE, related_name="ocorrencias")
    aluno = models.ForeignKey('Aluno', null=True, blank=True, on_delete=models.CASCADE, related_name="ocorrencias")
    trimestre = models.ForeignKey("Trimestre", on_delete=models.CASCADE, related_name="ocorrencias")
    
    tipo = models.CharField(max_length=2, choices=Tipo.choices, default=Tipo.OCORRENCIA) 

    def __str__(self):
        return f"{self.titulo} ({self.get_associado()})"
    
    def get_associado(self):
        if self.turma:
            return f"Turma: {self.turma.nome}"
        elif self.aluno:
            return f"Aluno: {self.aluno.nome}"
        return "Não associado"

    class Meta:
        ordering = ["-data_criacao"]  