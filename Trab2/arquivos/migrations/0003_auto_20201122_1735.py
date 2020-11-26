# Generated by Django 3.1.3 on 2020-11-22 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arquivos', '0002_auto_20201122_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arquivo',
            name='data',
            field=models.CharField(default='', max_length=10, verbose_name='Data de nascimento'),
        ),
        migrations.AlterField(
            model_name='arquivo',
            name='texto',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='arquivo',
            name='titulo',
            field=models.CharField(default='', help_text='Entre com o titulo', max_length=100),
        ),
    ]