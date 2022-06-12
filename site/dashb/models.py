from django.db import models
import datetime

class Top(models.Model):
    nome = models.CharField(max_length=50, null=True)

    def __str__(self) -> str:
        return self.nome

class Primavera(models.Model):
    nome_do_anime= models.CharField(max_length=50, null=True)


    def __str__(self) -> str:
        return self.nome_do_anime
    
class Verao(models.Model):
    nome_do_anime= models.CharField(max_length=50, null=True)


    def __str__(self) -> str:
        return self.nome_do_anime

class Outono(models.Model):
    nome_do_anime= models.CharField(max_length=50, null=True)


    def __str__(self) -> str:
        return self.nome_do_anime
    
class Inverno(models.Model):
    nome_do_anime= models.CharField(max_length=50, null=True)


    def __str__(self) -> str:
        return self.nome_do_anime

class MaisVisto(models.Model):
    nome_do_anime= models.CharField(max_length=50, null=True)
    qtd_views =models.IntegerField()
    
    def __str__(self) -> str:
        return self.nome_do_anime