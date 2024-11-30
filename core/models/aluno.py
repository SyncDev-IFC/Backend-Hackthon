from django.db import models
from .turma import Turma
# from .nota import Nota
class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    cpf = models.CharField(max_length=100)
    foto = models.ForeignKey('uploader.Image', on_delete=models.SET_NULL, null=True, blank=True, default=None, related_name='+')
    turma = models.ForeignKey(Turma, related_name="alunos", on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return f"{self.nome} - {self.matricula}"
    
    # def calcular_media(self):
    #     alunos = Aluno.objects.filter(turmas=self)
        
    #     if alunos.exists():
    #         total_notas = 0
    #         total_alunos = 0
            
    #         for aluno in alunos:
    #             notas = Nota.objects.filter(aluno=aluno)
    #             if notas.exists():
    #                 total_notas += sum([nota.valor for nota in notas])  
    #                 total_alunos += 1

    #         if total_alunos > 0:
    #             return total_notas / total_alunos
    #         else:
    #             return 0  
    #     else:
    #         return 0 