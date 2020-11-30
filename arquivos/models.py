from django.db import models
from django import forms
from django.core.validators import FileExtensionValidator

class Arquivo(models.Model):
    arquivo = models.FileField(validators=[FileExtensionValidator(allowed_extensions=['txt'])])
    
class Texto(models.Model):
    conteudo = models.TextField( default="")
    data =  models.CharField(max_length = 30,verbose_name='Data de criação',default="")
    titulo = models.CharField(max_length=100, help_text = "Entre com o titulo",default="")