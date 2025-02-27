from django.db import models


class Produto(models.Model):
    STATUS_CHOICES = [
        ('A', 'Ativo'),
        ('I', 'Inativo')
    ]
    
    TIPO_TRACAO_CHOICES = [
        ('D', 'Direcional'),
        ('T', 'Tração'),
        ('M', 'Misto'),
    ]
    
    CATEGORIA_CHOICES = [
        ('N', 'Novo'),
        ('R', 'Recapado'),
        ('C', 'Carcaça'),
    ]

    GRUPO_CHOICES = [
        ('B', 'Banda'),
        ('R', 'Reparo'),
        ('O', 'Outros'),
    ]
    
    descricao = models.CharField(max_length=200, verbose_name="Descrição")
    und = models.CharField(max_length=10, verbose_name="Unidade")
    grupo = models.CharField(max_length=1,
        choices=GRUPO_CHOICES,
        default='O'
    )
    subgrupo = models.CharField(max_length=100)
    tipo_tracao = models.CharField(
        max_length=1,
        choices=TIPO_TRACAO_CHOICES,
        verbose_name="Tipo de Tração"
    )
    cod_bandag = models.CharField(max_length=50, verbose_name="Código Bandag")
    tamanho = models.IntegerField(null=True, verbose_name="Tamanho")
       
    categoria = models.CharField(
        max_length=1,
        choices=CATEGORIA_CHOICES
    )
    status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        default='A'
    )

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['descricao']

    def __str__(self):
        return self.descricao


