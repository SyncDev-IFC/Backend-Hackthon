from django.db import models
from uploader.models import Image

class Curso(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    image = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.SET_NULL,
        default=None,
        blank=True,
        null=True
    )
    cor = models.CharField(
        max_length=7, 
        default="#FFFFFF", 
        help_text="Insira a cor em formato hexadecimal (ex: #FFFFFF)"
    )

    def __str__(self):
        return self.nome
