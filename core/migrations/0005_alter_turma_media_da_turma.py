# Generated by Django 5.1.3 on 2024-11-30 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_turma_media_da_turma"),
    ]

    operations = [
        migrations.AlterField(
            model_name="turma",
            name="media_da_turma",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]