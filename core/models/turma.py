from django.db import models
from .disciplina import Disciplina
from .curso import Curso
from uploader.models import Image

class Turma(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField(blank=True, null=True)
    ano_letivo = models.PositiveIntegerField()
    numero_estudantes = models.PositiveIntegerField(default=0)
    data_criacao = models.DateTimeField(auto_now_add=True)
    ultima_atualizacao = models.DateTimeField(auto_now=True)
    image = models.ForeignKey(Image, related_name="+", on_delete=models.SET_NULL, null=True, blank=True, default=None)
    disciplinas = models.ManyToManyField(Disciplina, related_name="turmas")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, null=True, blank=True)
    media_da_turma = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        ordering = ["ano_letivo", "nome"]

    def __str__(self):
        return f"{self.nome} ({self.ano_letivo})"
    
    def calcular_media_da_turma(self):
        """
        Calcula a média da turma com base nas notas dos alunos dessa turma.
        """
        from core.models import Aluno, Nota

        alunos = Aluno.objects.filter(turma=self)  
        if alunos.exists():
            total_notas = 0
            total_alunos = 0
            
            for aluno in alunos:
                notas = Nota.objects.filter(aluno=aluno, disciplina__in=self.disciplinas.all())
                
                if notas.exists():
                    total_notas += sum(nota.nota for nota in notas) / len(notas)
                    total_alunos += 1

            if total_alunos > 0:
                media_turma = total_notas / total_alunos
                self.media_da_turma = media_turma
                self.save()
                return media_turma
            else:
                return 0
        else:
            return 0