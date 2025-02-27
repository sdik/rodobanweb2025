# Generated by Django 5.1.6 on 2025-02-19 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vendedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('apelido', models.CharField(blank=True, max_length=50)),
                ('telefone', models.CharField(max_length=15)),
                ('senha', models.CharField(max_length=15)),
                ('percentual_comissao', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Percentual de Comissão (%)')),
            ],
            options={
                'verbose_name': 'Vendedor',
                'verbose_name_plural': 'Vendedores',
            },
        ),
    ]
