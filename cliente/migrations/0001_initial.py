# Generated by Django 5.1.6 on 2025-02-18 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_pessoa', models.CharField(choices=[('F', 'Física'), ('J', 'Jurídica')], max_length=1, verbose_name='Tipo de Pessoa')),
                ('data_cadastro', models.DateTimeField(auto_now_add=True, verbose_name='Data de Cadastro')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('cep', models.CharField(max_length=9, verbose_name='CEP')),
                ('logradouro', models.CharField(max_length=100, verbose_name='Logradouro')),
                ('numero', models.CharField(max_length=10, verbose_name='Número')),
                ('complemento', models.CharField(blank=True, max_length=100, null=True, verbose_name='Complemento')),
                ('bairro', models.CharField(max_length=50, verbose_name='Bairro')),
                ('cidade', models.CharField(max_length=50, verbose_name='Cidade')),
                ('estado', models.CharField(max_length=2, verbose_name='Estado')),
                ('ibge', models.CharField(max_length=10, verbose_name='IBGE')),
                ('telefone', models.CharField(max_length=15, verbose_name='Telefone')),
                ('celular', models.CharField(max_length=15, verbose_name='Celular')),
                ('email', models.EmailField(max_length=100, verbose_name='E-mail')),
                ('nome', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nome Completo')),
                ('cpf', models.CharField(blank=True, max_length=14, null=True, unique=True, verbose_name='CPF')),
                ('rg', models.CharField(blank=True, max_length=20, null=True, verbose_name='RG')),
                ('data_nascimento', models.DateField(blank=True, null=True, verbose_name='Data de Nascimento')),
                ('estado_civil', models.CharField(blank=True, choices=[('S', 'Solteiro(a)'), ('C', 'Casado(a)'), ('D', 'Divorciado(a)'), ('V', 'Viúvo(a)')], max_length=1, null=True, verbose_name='Estado Civil')),
                ('profissao', models.CharField(blank=True, max_length=50, null=True, verbose_name='Profissão')),
                ('razao_social', models.CharField(blank=True, max_length=100, null=True, verbose_name='Razão Social')),
                ('nome_fantasia', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nome Fantasia')),
                ('cnpj', models.CharField(blank=True, max_length=18, null=True, unique=True, verbose_name='CNPJ')),
                ('inscricao_estadual', models.CharField(blank=True, max_length=20, null=True, verbose_name='Inscrição Estadual')),
                ('inscricao_municipal', models.CharField(blank=True, max_length=20, null=True, verbose_name='Inscrição Municipal')),
                ('responsavel', models.CharField(blank=True, max_length=100, null=True, verbose_name='Responsável')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'ordering': ['nome', 'razao_social'],
            },
        ),
    ]
