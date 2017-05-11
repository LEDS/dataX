from __future__ import unicode_literals

from django.db import models
from app_organizacional.models import *

class Cor (models.Model):
    nome = models.CharField(max_length=50)
    sigla = models.CharField(max_length=3)
    class Meta:
        db_table = 'Cor'

class Sexo (models.Model):
    nome = models.CharField(max_length=50)
    sigla = models.CharField(max_length=1)
    class Meta:
        db_table = 'Sexo'

class Renda_Familiar(models.Model):
    descricao = models.CharField(max_length=50)
    codigo  = models.IntegerField()
    class Meta:
        db_table = 'Renda_Familiar'

class Tipo_Escola_Origem(models.Model):
    descricao = models.CharField(max_length=50)
    codigo = models.CharField(max_length=1)
    class Meta:
        db_table = 'Tipo_Escola_Origem'

class Forma_Ingresso(models.Model):
    nome = models.CharField(max_length=400)
    sigla = models.CharField(max_length=50)
    class Meta:
        db_table = 'Forma_Ingresso'

class Responsavel(models.Model):
    nome = models.CharField(max_length=50)
    class Meta:
        db_table = 'Responsavel'

class Reside(models.Model):
    nome = models.CharField(max_length=50)
    class Meta:
        db_table = 'Reside'

class Profissao(models.Model):
    nome = models.CharField(max_length=50)
    class Meta:
        db_table = 'Profissao'

class Pessoa(models.Model):
    ano_nascimento = models.IntegerField(blank=True,null=True,)
    ano_conclusao_ensino_medio = models.IntegerField(blank=True,null=True,)
    ano_conclusao_primeiro_grau  = models.IntegerField(blank=True,null=True,)

    codigo_social = models.CharField(max_length=255)
    ano_reservista = models.IntegerField(blank=True, null=True, )
    cor = models.ForeignKey(Cor)
    sexo = models.ForeignKey(Sexo)

    #estado_civil_pais =
    #escolaridade_pai =
    #escolaridade_mae =
    pai_falecido = models.BooleanField(default=False)
    mae_falecido = models.BooleanField(default=False)
    tipo_responsavel = models.ForeignKey(Responsavel)
    reside = models.ForeignKey(Reside)

    necessidade_fisica = models.BooleanField(default=False)
    necessidade_auditiva = models.BooleanField(default=False)
    necessidade_mental = models.BooleanField(default=False)
    necessidade_multipla = models.BooleanField(default=False)
    superdotado = models.BooleanField(default=False)
    profissao = models.ForeignKey(Profissao)
    #numero_filhos =
    ano_reservista = models.IntegerField(blank=True,null=True,)
    bolsa_familia = models.BooleanField(default=False)
    class Meta:
        db_table = 'Pessoa'


class Escola_Origem_Pessoa(models.Model):
    pessoa = models.ForeignKey(Pessoa)
    tipo_escola_origem = models.ForeignKey(Tipo_Escola_Origem)
    ano = models.IntegerField(blank=True, null=True,)
    class Meta:
        db_table = 'Escola_Origem_Pessoa'

class Renda_Familiar_Pessoa(models.Model):
    pessoa = models.ForeignKey(Pessoa)
    renda_familiar = models.ForeignKey(Renda_Familiar)
    ano = models.IntegerField(blank=True, null=True,)
    class Meta:
        db_table = 'Renda_Familiar_Pessoa'

class Forma_Ingresso_Pessoa(models.Model):
    pessoa = models.ForeignKey(Pessoa)
    forma_ingresso = models.ForeignKey(Forma_Ingresso)
    ano = models.IntegerField(blank=True, null=True, )
    class Meta:
        db_table = 'Forma_Ingresso_Pessoa'

class Endereco (models.Model):
    cep = models.CharField(max_length=50,blank=True,null=True,)
    pessoa = models.ForeignKey(Pessoa)
    class Meta:
        db_table = 'Endereco'