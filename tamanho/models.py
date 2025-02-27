from django.db import models

# Create your models here.

class Tamanho(models.Model):
    STATUS_CHOICES = [
        ('A', 'Ativo'),
        ('I', 'Inativo')
    ]
    
    medida = models.CharField(max_length=50)
    status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        default='A'
    )
    
    class Meta:
        verbose_name = 'Tamanho'
        verbose_name_plural = 'Tamanhos'
        ordering = ['medida']
    
    def __str__(self):
        return self.medida
