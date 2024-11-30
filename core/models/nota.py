from django.db import models
from core.models import Aluno, Disciplina, Trimestre

class Nota(models.Model):
    nota = models.DecimalField(max_digits=5, decimal_places=2)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name='notas')
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, related_name='notas')
    trimestre = models.ForeignKey(Trimestre, on_delete=models.CASCADE, related_name='notas')


    def __self__(self):
        return f"{self.aluno.nome} - {self.disciplina.nome} - {self.trimestre.nome}"
    