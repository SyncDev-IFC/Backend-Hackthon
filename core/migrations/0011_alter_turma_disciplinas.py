# Generated by Django 5.1.3 on 2024-11-29 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0010_user_reset_code"),
    ]

    operations = [
        migrations.AlterField(
            model_name="turma",
            name="disciplinas",
            field=models.ManyToManyField(related_name="turmas", to="core.disciplina"),
        ),
    ]