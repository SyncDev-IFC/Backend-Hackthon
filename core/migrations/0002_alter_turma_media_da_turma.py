# Generated by Django 5.1.3 on 2024-11-29 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="turma",
            name="media_da_turma",
            field=models.FloatField(blank=True, null=True),
        ),
    ]
