from django.db import models

# Create your models here.
class Selo(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='selos/') 
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
    
class Atividade(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    data_atividade = models.DateField()

    def __str__(self):
        return self.nome

class Pessoa(models.Model):
    nome = models.CharField(max_length=45)
    idade = models.IntegerField()
    email = models.CharField(max_length=60, unique=True)
    
    def __str__(self):
        return self.nome

class PessoaAtividade(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, related_name='atividades_realizadas')
    atividade = models.ForeignKey(Atividade, on_delete=models.CASCADE)
    data_realizacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.pessoa.nome} - {self.atividade.nome}"