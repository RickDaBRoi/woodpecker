# Generated by Django 2.2.4 on 2019-08-30 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Timber', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ferramenta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('descricao', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Madeira',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('cor', models.CharField(max_length=20)),
                ('descricao', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='estado',
            name='sigla',
            field=models.CharField(max_length=2, unique=True, verbose_name='Sigla: '),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='email',
            field=models.CharField(help_text='Digite seu e-mail', max_length=100, verbose_name='Email: '),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='nascimento',
            field=models.DateField(verbose_name='Data de Nascimento: '),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='nome',
            field=models.CharField(help_text='Digite seu nome completo', max_length=50, verbose_name='Nome: '),
        ),
    ]
