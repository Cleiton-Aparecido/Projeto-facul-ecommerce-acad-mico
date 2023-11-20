# myapp/models.py
from django.db import models
from django.contrib.auth.models import User
from django.db import models


class Instituicoes(models.Model):
    nome = models.CharField(max_length=150)
    municipio = models.CharField(max_length=150)
    sigla   = models.CharField(max_length=20)
    def __str__(self):
        return f'{self.nome} {self.municipio}'

class Itens(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=700)
    valor = models.FloatField()
    quantidade = models.IntegerField()

    def __str__(self):
        return f'{self.nome} {self.descricao}'

class Pagamentos(models.Model):
    sigla = models.CharField(max_length=3)
    nome = models.CharField(max_length=50)

class Compras(models.Model):
    quantidade = models.IntegerField()
    user = models.ForeignKey(User,  on_delete=models.CASCADE)
    item = models.ForeignKey(Itens, on_delete=models.CASCADE)
    pagamento = models.ForeignKey(Pagamentos, on_delete=models.CASCADE)

class Carrinhos(models.Model):
    quantidade = models.IntegerField()
    user = models.ForeignKey(User,  on_delete=models.CASCADE)
    item = models.ForeignKey(Itens, on_delete=models.CASCADE)

class Vendas(models.Model):
    quantidade = models.IntegerField()
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Itens, on_delete=models.CASCADE)

class FormasDePagamentos(models.Model):
    item = models.ForeignKey(Itens, on_delete=models.CASCADE)
    pagamento = models.ForeignKey(Pagamentos, on_delete=models.CASCADE)

class Imagens(models.Model):
    descricao = models.CharField(max_length=200)
    imagem = models.ImageField(upload_to='imagens/')
    item = models.ForeignKey(Itens, on_delete=models.CASCADE)

class Comentarios(models.Model):
    descricao = models.CharField(max_length=200)
    idComentarioResposta = models.IntegerField()
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Itens, on_delete=models.CASCADE)

class Curtidas(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Itens, on_delete=models.CASCADE)
