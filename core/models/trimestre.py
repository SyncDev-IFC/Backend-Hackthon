from django.db import models

class Trimestre(models.Model):
    class TrimestreName(models.IntegerChoices):
        PRIMEIRO = 1, "Primeiro Trimestre",
        SEGUNDO = 2, "Segundo Trimestre",
        TERCEIRO = 3, "Terceiro Trimestre"

    name = models.IntegerField(choices=TrimestreName.choices, unique=True)
    ano = models.PositiveIntegerField()
    def __str__(self):
        return f"{self.name}"