from django.db import models

class Vendedor(models.Model):
    nome = models.CharField(max_length=50)    
    apelido = models.CharField(max_length=50, blank=True)
    telefone = models.CharField(max_length=15)
    senha = models.CharField(max_length=15)
    email = models.EmailField(blank=True)
    percentual_comissao = models.DecimalField(
        max_digits=5, 
        decimal_places=2,
        verbose_name="Percentual de Comissão (%)"
    )

    class Meta:
        verbose_name = "Vendedor"
        verbose_name_plural = "Vendedores"

    def __str__(self):
        return f"{self.nome} ({self.apelido})" if self.apelido else self.nome