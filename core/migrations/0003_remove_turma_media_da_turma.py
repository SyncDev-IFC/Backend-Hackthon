# Generated by Django 5.1.3 on 2024-11-29 22:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_alter_turma_media_da_turma"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="turma",
            name="media_da_turma",
        ),
    ]
