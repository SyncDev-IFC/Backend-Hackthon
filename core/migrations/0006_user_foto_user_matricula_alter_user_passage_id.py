# Generated by Django 5.1.2 on 2024-11-29 00:17

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_user_passage_id'),
        ('uploader', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='foto',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='uploader.image'),
        ),
        migrations.AddField(
            model_name='user',
            name='matricula',
            field=models.PositiveIntegerField(default=None, help_text='Matrícula do aluno', unique=True, verbose_name='matricula'),
        ),
        migrations.AlterField(
            model_name='user',
            name='passage_id',
            field=models.CharField(default=uuid.uuid4, help_text='Passage ID', max_length=255, unique=True, verbose_name='passage_id'),
        ),
    ]
