# Generated by Django 2.1.7 on 2019-09-06 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Timber', '0002_auto_20190830_2032'),
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Informe o nome do material', max_length=30, verbose_name='Nome: ')),
                ('descricao', models.CharField(max_length=50, verbose_name='Descrição: ')),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Informe o nome do produto', max_length=30, verbose_name='Nome: ')),
                ('tipo', models.CharField(help_text='Informe o tipo do produto', max_length=30, verbose_name='Tipo: ')),
                ('descricao', models.CharField(max_length=50, verbose_name='Descrição: ')),
            ],
        ),
        migrations.AlterField(
            model_name='cidade',
            name='nome',
            field=models.CharField(help_text='Digite o nome da sua cidade', max_length=50, verbose_name='Nome: '),
        ),
        migrations.AlterField(
            model_name='estado',
            name='nome',
            field=models.CharField(help_text='Digite o nome do seu estado', max_length=50, verbose_name='Nome: '),
        ),
        migrations.AlterField(
            model_name='ferramenta',
            name='descricao',
            field=models.CharField(max_length=100, verbose_name='Descrição: '),
        ),
        migrations.AlterField(
            model_name='ferramenta',
            name='nome',
            field=models.CharField(help_text='Digite o nome da ferramenta', max_length=30, verbose_name='Nome: '),
        ),
        migrations.AlterField(
            model_name='madeira',
            name='cor',
            field=models.CharField(help_text='Digite a cor da madeira', max_length=20, verbose_name='Cor: '),
        ),
        migrations.AlterField(
            model_name='madeira',
            name='descricao',
            field=models.CharField(max_length=100, verbose_name='Descrição: '),
        ),
        migrations.AlterField(
            model_name='madeira',
            name='nome',
            field=models.CharField(help_text='Digite o nome da madeira', max_length=50, verbose_name='Nome: '),
        ),
    ]
