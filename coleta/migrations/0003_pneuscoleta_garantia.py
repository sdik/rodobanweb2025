# Generated by Django 5.1.6 on 2025-02-24 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coleta', '0002_alter_pneuscoleta_fabricante'),
    ]

    operations = [
        migrations.AddField(
            model_name='pneuscoleta',
            name='garantia',
            field=models.BooleanField(default=False),
        ),
    ]
