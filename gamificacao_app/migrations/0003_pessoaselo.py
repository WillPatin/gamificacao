# Generated by Django 5.1 on 2024-11-04 23:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamificacao_app', '0002_pessoa'),
    ]

    operations = [
        migrations.CreateModel(
            name='PessoaSelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_ganho', models.DateTimeField(auto_now_add=True)),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gamificacao_app.pessoa')),
                ('selo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gamificacao_app.selo')),
            ],
        ),
    ]
