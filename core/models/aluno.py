from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    cpf = models.CharField(max_length=100)
    foto = models.ForeignKey('uploader.Image', on_delete=models.SET_NULL, null=True, blank=True, default=None, related_name='+')

    def __str__(self):
        return f"{self.nome} - {self.matricula}"