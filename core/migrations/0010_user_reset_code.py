# Generated by Django 5.1.3 on 2024-11-29 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0009_turma_curso"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="reset_code",
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
    ]