from django.db import models

# Create your models here.

class Eventos(models.Model):

    nome = models.CharField(max_length=80)
    tema = models.CharField(max_length=80)
    descricao = models.CharField(max_length=5000)
    data = models.DateField
    hora = models.TimeField
    organizador = models.CharField(max_length=80)
    telefone = models.CharField(max_length=15)
    email = models.EmailField

def __str__(self):

    return self.nome

class Tipo_user(models.Model):
    descricao = models.CharField(max_length=45)

def __str__ (self):

    return self.descricao

class Grupo_de_estudos(models.Model):
    materia = models.CharField(max_length=45)
    horario = models.TimeField
    local = models.CharField(max_length=45)
    dia = models.DateField

def __str__ (self):

    return self.materia

class Comite(models.Model):
    nome = models.CharField(max_length=80)
    pauta = models.CharField(max_length=150)
    sala = models.CharField(max_length=20)
    responsavel = models.CharField(max_length=80)

def __str__(self):

    return self.nome

class Comissao(models.Model):
    nome = models.CharField(max_length=80)
    pauta = models.CharField(max_length=150)
    sala = models.CharField(max_length=20)
    responsavel = models.CharField(max_length=80)

def __str__(self):

    return self.nome

class Nucleos(models.Model):
    nome = models.CharField(max_length=80)
    pauta = models.CharField(max_length=150)
    sala = models.CharField(max_length=20)
    responsavel = models.CharField(max_length=80)

def __str__(self):

    return self.nome

class User(models.Model):
    nome = models.CharField(max_length=80)
    data_nascimento = models.DateField
    email = models.EmailField
    login = models.CharField(max_length=120)
    telefone = models.CharField(max_length=15)
    senha = models.CharField(max_length=30)
    tipo_user = models.ForeignKey(Tipo_user, on_delete=models.PROTECT)

def __str__(self):

    return self.nome

class Atendimento(models.Model):
    nome = models.CharField(max_length=80)
    data = models.DateField
    hora = models.TimeField
    local = models.CharField(max_length=50)
    nome_produto = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

def __str__(self):

    return self.nome

class Vendas(models.Model):
    nome = models.CharField(max_length=80)
    data = models.DateField
    hora = models.TimeField
    local = models.CharField(max_length=50)
    nome_produto = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete = models.PROTECT)

def __str__(self):

    return self.nome

class Reservar(models.Model):
    data = models.DateField
    atendimento = models.CharField(max_length=45)
    venda = models.CharField(max_length=45)
    user = models.ForeignKey(User, on_delete = models.PROTECT)
    vendas = models.ForeignKey(Vendas, on_delete = models.PROTECT)
    atendimento = models.ForeignKey(Atendimento, on_delete = models.PROTECT)

def __str__(self):

    return self.user

class User_eventos(models.Model):
    user = models.ForeignKey(User, on_delete = models.PROTECT)
    eventos = models.ForeignKey(Eventos, on_delete = models.PROTECT)

def __str__(self):
        
        return f'{self.user} - {self.eventos}'

class User_grupo(models.Model):
    user = models.ForeignKey(User, on_delete = models.PROTECT)
    grupo_de_estudos = models.ForeignKey(Grupo_de_estudos, on_delete = models.PROTECT)

def __str__(self):
        
        return f'{self.user} - {self.grupo_de_estudos}'

class User_comite(models.Model):
    user = models.ForeignKey(User, on_delete = models.PROTECT)
    comite = models.ForeignKey(Comite, on_delete = models.PROTECT)

def __str__(self):
        
        return f'{self.user} - {self.comite}'

class User_comissao(models.Model):
    user = models.ForeignKey(User, on_delete = models.PROTECT)
    comissao = models.ForeignKey(Comissao, on_delete = models.PROTECT)

def __str__(self):
        
        return f'{self.user} - {self.comissao}'

class User_nucleos(models.Model):
    user = models.ForeignKey(User, on_delete = models.PROTECT)
    nucleos = models.ForeignKey(Nucleos, on_delete = models.PROTECT)

def __str__(self):
        
        return f'{self.user} - {self.nucleos}'