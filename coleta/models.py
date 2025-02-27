from django.db import models
from cliente.models import Cliente
from vendedor.models import Vendedor
from produto.models import Produto
from tamanho.models import Tamanho
from fabricante.models import Fabricante

# Create your models here.

class Coleta(models.Model):
    FORMA_PAGAMENTO_CHOICES = [
        ('AV', 'À Vista'),
        ('AP', 'A Prazo'),
        ('CC', 'Cartão de Crédito'),
        ('CD', 'Cartão de Débito'),
        ('PIX', 'PIX'),
    ]

    data = models.DateField(auto_now_add=True)
    numero_apanha = models.CharField(max_length=20, unique=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.PROTECT)
    forma_pagamento = models.CharField(
        max_length=3,
        choices=FORMA_PAGAMENTO_CHOICES,
        default='AV'
    )
    
    def __str__(self):
        return f"Coleta {self.numero_apanha} - {self.cliente}"
    
    class Meta:
        verbose_name = 'Coleta'
        verbose_name_plural = 'Coletas'
        ordering = ['-data']

class PneusColeta(models.Model):
    coleta = models.ForeignKey(Coleta, on_delete=models.CASCADE, related_name='pneus')
    serie = models.CharField(max_length=50)
    fogo = models.CharField(max_length=50)
    tamanho = models.ForeignKey(
        Tamanho,
        on_delete=models.PROTECT,
        limit_choices_to={'status': 'A'}
    )
    desenho = models.ForeignKey(
        Produto, 
        on_delete=models.PROTECT,
        limit_choices_to={'grupo': 'B'}  # Limita apenas a produtos do grupo Banda
    )
    fabricante = models.ForeignKey(
        Fabricante,
        on_delete=models.PROTECT,
        limit_choices_to={'status': 'A'}
    )
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    montado = models.BooleanField(default=False)
    garantia = models.BooleanField(default=False)
    observacao = models.TextField(blank=True)
    

    #calular valor total da coleta
    def calcular_valor_total(self):
        total = self.coleta.pneus.aggregate(total=models.Sum('valor'))['total'] or 0.00
        return total
    
    def __str__(self):
        return f"Pneu {self.serie} - {self.tamanho}"
    
    class Meta:
        verbose_name = 'Pneu da Coleta'
        verbose_name_plural = 'Pneus da Coleta'
        ordering = ['serie']
