# Generated by Django 3.1.3 on 2020-11-30 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arquivos', '0008_auto_20201129_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='texto',
            name='data',
            field=models.CharField(default='', max_length=20, verbose_name='Data de criação'),
        ),
    ]