from django.db import models
from datetime import datetime

# Create your models here.

class Assinante(models.Model):
    cpf_cnpj = models.IntegerField(u'CPF ou CNPJ', unique=True)
    nome = models.CharField(u'Nome', max_length=100)
    cep = models.IntegerField(u'CEP')
    endereco = models.CharField(u'Endereço', max_length=100)
    numero = models.IntegerField(u'Número')
    bairro = models.CharField(u'Bairro', max_length=40)
    cidade = models.CharField(u'Cidade', max_length=40)
    estado = models.CharField(u'Estado', max_length=2)
    fone = models.IntegerField(u'Fone')
    email = models.EmailField(u'E-mail')
    contato = models.CharField(u'Contato', max_length=100)

    def __str__(self):
        return self.nome

class Unidade(models.Model):
    nome =  models.CharField(u'Nome', max_length=100)
    ha_fisico = models.IntegerField(u'Ha físico')
    assinante = models.ForeignKey(Assinante, verbose_name='Assinante', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Safra(models.Model):
    descricao = models.CharField(u'Descrição', max_length=40)
    assinante = models.ForeignKey(Assinante, verbose_name='Assinante', on_delete=models.CASCADE)
    dt_inicio = models.DateField(u'Data Inicial')
    dt_final  = models.DateField(u'Data Final')

    def __str__(self):
        return self.nome

class Cultura(models.Model):
    nome = models.CharField(u'Nome', max_length=20)

    def __str__(self):
        return self.nome

class Ccusto(models.Model):
    descricao = models.CharField(u'Descrição', max_length=20)
    assinante = models.ForeignKey(Assinante, verbose_name='Assinante', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Pcontas(models.Model):
    TIPO_CHOICES = (
        ('S', 'Sintetica'),
        ('A', 'Analitica'),
    )
    SN_CHOICES = (
        ('S', 'Sim'),
        ('N', 'Não'),
    )
    codigo = models.IntegerField(u'Código', unique=True)
#    reduzido = models.AutoField(primary_key=False, editable=False, verbose_name='Código Reduzido')
    descricao = models.CharField(u'Descrição', max_length=50)
    tipo = models.CharField(u'Tipo', max_length=1, choices = TIPO_CHOICES, default='A')
    grupo = models.CharField(u'Grupo', max_length=1, choices = SN_CHOICES, default='N')
    dre = models.CharField(u'DRE', max_length=1, choices = SN_CHOICES, default='N')
#    assinante = models.ForeignKey(Assinante, verbose_name='Assinante', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
