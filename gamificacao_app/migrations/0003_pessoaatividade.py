# Generated by Django 5.1 on 2024-11-04 23:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamificacao_app', '0002_pessoa'),
    ]

    operations = [
        migrations.CreateModel(
            name='PessoaAtividade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_realizacao', models.DateTimeField(auto_now_add=True)),
                ('atividade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gamificacao_app.atividade')),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='atividades_realizadas', to='gamificacao_app.pessoa')),
            ],
        ),
    ]
