from django.db import models

# Create your models here.
class Arquivo(models.Model):
    texto = models.CharField(max_length = 1000,default="")
    data =  models.CharField(max_length = 10,verbose_name='Data de nascimento',default="")
    titulo = models.CharField(max_length=100, help_text = "Entre com o titulo",default="")