# Generated by Django 2.2.5 on 2019-09-20 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_biblioteca', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimo',
            name='data_efetiva_devolucao',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
