# Generated by Django 5.1 on 2024-11-04 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Atividade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('data_atividade', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Selo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('descricao', models.TextField()),
                ('imagem', models.ImageField(upload_to='selos/')),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]