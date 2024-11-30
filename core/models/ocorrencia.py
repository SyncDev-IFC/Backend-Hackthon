from django.db import models
from django.forms import CharField

class Ocorrencia(models.Model):
    class Tipo(models.TextChoices):
        Atraso = 1, 'Atraso de Aluno'
        Uniforme = 2, 'Aluno sem Uniforme'
        Reuniao = 3, 'Reunião com Nupe'
        Outro = 4, 'Outro'
    
    titulo = models.CharField(max_length=100)  
    conteudo = models.TextField() 
    data_criacao = models.DateTimeField(auto_now_add=True)  
    aluno = models.ForeignKey('Aluno', null=True, blank=True, on_delete=models.CASCADE, related_name="ocorrencias")
    trimestre = models.ForeignKey("Trimestre", on_delete=models.CASCADE, related_name="ocorrencias", null=True, blank=True)
    outro_tipo = models.CharField(max_length=100, null=True, blank=True)
    
    tipo = models.CharField(max_length=2, choices=Tipo.choices,) 

    def __str__(self):
        return f"{self.titulo} ({self.get_associado()})"
    
    def get_associado(self):
        if self.turma:
            return f"Turma: {self.aluno.turma.nome}"
        elif self.aluno:
            return f"Aluno: {self.aluno.nome}"
        return "Não associado"

    class Meta:
        ordering = ["-data_criacao"]  