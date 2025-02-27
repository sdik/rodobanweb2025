from django.db import models

class Cliente(models.Model):
    TIPO_PESSOA_CHOICES = [
        ('F', 'Física'),
        ('J', 'Jurídica'),
    ]

    ESTADO_CIVIL_CHOICES = [
        ('S', 'Solteiro(a)'),
        ('C', 'Casado(a)'),
        ('D', 'Divorciado(a)'),
        ('V', 'Viúvo(a)'),
    ]

    # Campos comuns para ambos os tipos
    tipo_pessoa = models.CharField('Tipo de Pessoa', max_length=1, choices=TIPO_PESSOA_CHOICES)
    data_cadastro = models.DateTimeField('Data de Cadastro', auto_now_add=True)
    ativo = models.BooleanField('Ativo', default=True)
    
    # Campos de endereço
    cep = models.CharField('CEP', max_length=9)
    logradouro = models.CharField('Logradouro', max_length=100)
    numero = models.CharField('Número', max_length=10)
    complemento = models.CharField('Complemento', max_length=100, blank=True, null=True)
    bairro = models.CharField('Bairro', max_length=50)
    cidade = models.CharField('Cidade', max_length=50)
    estado = models.CharField('Estado', max_length=2)
    ibge = models.CharField('IBGE', max_length=10)
    
    # Campos de contato
    telefone = models.CharField('Telefone', max_length=15)
    celular = models.CharField('Celular', max_length=15)
    email = models.EmailField('E-mail', max_length=100)
    
    # Campos específicos para Pessoa Física
    nome = models.CharField('Nome Completo', max_length=100, blank=True, null=True)
    cpf = models.CharField('CPF', max_length=14, blank=True, null=True, unique=True)
    rg = models.CharField('RG', max_length=20, blank=True, null=True)
    data_nascimento = models.DateField('Data de Nascimento', blank=True, null=True)
    estado_civil = models.CharField('Estado Civil', max_length=1, choices=ESTADO_CIVIL_CHOICES, blank=True, null=True)
    profissao = models.CharField('Profissão', max_length=50, blank=True, null=True)
    
    # Campos específicos para Pessoa Jurídica
    razao_social = models.CharField('Razão Social', max_length=100, blank=True, null=True)
    nome_fantasia = models.CharField('Nome Fantasia', max_length=100, blank=True, null=True)
    cnpj = models.CharField('CNPJ', max_length=18, blank=True, null=True, unique=True)
    inscricao_estadual = models.CharField('Inscrição Estadual', max_length=20, blank=True, null=True)
    inscricao_municipal = models.CharField('Inscrição Municipal', max_length=20, blank=True, null=True)
    responsavel = models.CharField('Responsável', max_length=100, blank=True, null=True)
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['nome', 'razao_social']

    def __str__(self):
        if self.tipo_pessoa == 'F':
            return self.nome or ''
        return self.razao_social or ''

    def clean(self):
        from django.core.exceptions import ValidationError
        
        # Validações para Pessoa Física
        if self.tipo_pessoa == 'F':
            if not self.nome:
                raise ValidationError('Nome é obrigatório para pessoa física')
            if not self.cpf:
                raise ValidationError('CPF é obrigatório para pessoa física')
            
        # Validações para Pessoa Jurídica
        if self.tipo_pessoa == 'J':
            if not self.razao_social:
                raise ValidationError('Razão Social é obrigatória para pessoa jurídica')
            if not self.cnpj:
                raise ValidationError('CNPJ é obrigatório para pessoa jurídica')

# Create your models here.
