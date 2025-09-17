from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Eventos(models.Model):

    nome = models.CharField(max_length=80)
    descricao = models.CharField(max_length=5000)
    data = models.DateField
    hora = models.TimeField
    organizador = models.CharField(max_length=80)
    telefone = models.CharField(max_length=15)
    email = models.EmailField

    def __str__(self):

        return f'{self.nome} - {self.organizador}'

    class Meta:
         
        verbose_name_plural = "Eventos"
        verbose_name = "Evento"

class Tipo_user(models.Model):
    descricao = models.CharField(max_length=45)

    def __str__ (self):

        return self.descricao
    
    class Meta:
         
        verbose_name_plural = "Tipos de usuários"
        verbose_name = "Tipo de usuário"

class Grupo_estudo(models.Model):
    materia = models.CharField(max_length=45)
    horario = models.TimeField
    local = models.CharField(max_length=45)
    dia = models.DateField

    def __str__ (self):

        return f'{self.materia} - {self.local}'
    
    class Meta:
         
        verbose_name_plural = "Grupos de estudos"
        verbose_name = "Grupo de Estudo"

class Comite(models.Model):
    nome = models.CharField(max_length=80)
    pauta = models.CharField(max_length=150)
    sala = models.CharField(max_length=20)
    responsavel = models.CharField(max_length=80)

    def __str__(self):

        return f'{self.nome} - {self.responsavel}: {self.pauta}'
    
    class Meta:
         
        verbose_name_plural = "Comites"
        verbose_name = "Comite"

class Comissao(models.Model):
    nome = models.CharField(max_length=80)
    pauta = models.CharField(max_length=150)
    sala = models.CharField(max_length=20)
    responsavel = models.CharField(max_length=80)

    def __str__(self):

        return f'{self.nome} - {self.responsavel}: {self.pauta}'
    
    class Meta:
         
        verbose_name_plural = "Comissões"
        verbose_name = "Comissão"

class Nucleos(models.Model):
    nome = models.CharField(max_length=80)
    pauta = models.CharField(max_length=150)
    sala = models.CharField(max_length=20)
    responsavel = models.CharField(max_length=80)

    def __str__(self):

        return f'{self.nome} - {self.responsavel}: {self.pauta}'
    
    class Meta:
         
        verbose_name_plural = "Núcleos"
        verbose_name = "Núcleo"

class User(AbstractUser):
    first_name = None
    last_name = None
    nome = models.CharField(max_length=80, blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    username = models.CharField(max_length=120, unique=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    tipo_user = models.ForeignKey(Tipo_user, on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):

        return f'{self.nome} - {self.username}'
    
    class Meta:
         
        verbose_name_plural = "Usuários"
        verbose_name = "Usuário"

class Atendimento(models.Model):
    nome = models.CharField(max_length=80)
    data = models.DateField
    hora = models.TimeField
    local = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):

        return f'{self.nome} - {self.user} '
    
    class Meta:
         
        verbose_name_plural = "Atendimentos"
        verbose_name = "Atendimento"

class Vendas(models.Model):
    nome = models.CharField(max_length=80)
    data = models.DateField
    hora = models.TimeField
    local = models.CharField(max_length=50)
    preco = models.CharField(max_length=9)
    nome_produto = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete = models.PROTECT)

    def __str__(self):

        return f'{self.nome} - {self.preco}'
    
    class Meta:
         
        verbose_name_plural = "Vendas"
        verbose_name = "Venda"

class Reservar(models.Model):
    data = models.DateField
    atendimento = models.CharField(max_length=45)
    venda = models.CharField(max_length=45)
    user = models.ForeignKey(User, on_delete = models.PROTECT)
    vendas = models.ForeignKey(Vendas, on_delete = models.PROTECT)
    atendimento = models.ForeignKey(Atendimento, on_delete = models.PROTECT)

    def __str__(self):

        return f'{self.user} /n {self.vendas} /n {self.atendimento}'
    
    class Meta:
         
        verbose_name_plural = "Reservas"
        verbose_name = "Reserva"

class User_eventos(models.Model):
    user = models.ForeignKey(User, on_delete = models.PROTECT)
    eventos = models.ForeignKey(Eventos, on_delete = models.PROTECT)

    def __str__(self):
            
            return f'{self.user} - {self.eventos}'
    
    class Meta:
         
        verbose_name_plural = "Eventos dos Usúario"
        verbose_name = "Evento do Usuário"

class User_grupo(models.Model):
    user = models.ForeignKey(User, on_delete = models.PROTECT)
    grupo_de_estudos = models.ForeignKey(Grupo_estudo, on_delete = models.PROTECT)

    def __str__(self):
            
            return f'{self.user} - {self.grupo_de_estudos}'
    
    class Meta:
         
        verbose_name_plural = "Grupos de Estudo do Usuário"
        verbose_name = "Grupo de Estudo do Usuário"

class User_comite(models.Model):
    user = models.ForeignKey(User, on_delete = models.PROTECT)
    comite = models.ForeignKey(Comite, on_delete = models.PROTECT)

    def __str__(self):
            
            return f'{self.user} - {self.comite}'
    
    class Meta:
         
        verbose_name_plural = "Comites do Usuário"
        verbose_name = "Comite do Usuário"

class User_comissao(models.Model):
    user = models.ForeignKey(User, on_delete = models.PROTECT)
    comissao = models.ForeignKey(Comissao, on_delete = models.PROTECT)

    def __str__(self):
            
            return f'{self.user} - {self.comissao}'
    
    class Meta:
         
        verbose_name_plural = "Comissões do Usuário"
        verbose_name = "Comissão do Usuário"

class User_nucleos(models.Model):
    user = models.ForeignKey(User, on_delete = models.PROTECT)
    nucleos = models.ForeignKey(Nucleos, on_delete = models.PROTECT)

    def __str__(self):
            
            return f'{self.user} - {self.nucleos}'
    
    class Meta:
         
        verbose_name_plural = "Núcleos do Usuário"
        verbose_name = "Núcleo do Usuário"