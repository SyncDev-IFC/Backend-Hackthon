from django.db import models

class Trimestre(models.Model):
    class TrimestreName(models.IntegerChoices):
        PRIMEIRO = 1, "1 Trimestre",
        SEGUNDO = 2, "2 Trimestre",
        TERCEIRO = 3, "3 Trimestre"

    name = models.IntegerField(choices=TrimestreName.choices, unique=True)
    ano = models.PositiveIntegerField()
    def __str__(self):
        return f"self.name"