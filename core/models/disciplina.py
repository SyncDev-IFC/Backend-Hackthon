from django.db import models
from .user import User 

class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    carga_horaria = models.IntegerField()
    professor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, default=None, related_name='disciplinas')

    def __str__(self):
        return f"{self.nome}"