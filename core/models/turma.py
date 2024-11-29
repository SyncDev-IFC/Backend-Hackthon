from django.db import models
from core.models import Disciplina
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
    

    class Meta:
        ordering = ["ano_letivo", "nome"]  

    def __str__(self):
        return f"{self.nome} ({self.ano_letivo})"
