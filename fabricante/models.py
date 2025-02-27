from django.db import models

# Create your models here.

class Fabricante(models.Model):
    STATUS_CHOICES = [
        ('A', 'Ativo'),
        ('I', 'Inativo')
    ]
    
    nome = models.CharField(max_length=100)
    status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        default='A'
    )
    
    class Meta:
        verbose_name = 'Fabricante'
        verbose_name_plural = 'Fabricantes'
        ordering = ['nome']
    
    def __str__(self):
        return self.nome
