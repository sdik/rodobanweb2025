from django import forms
from .models import Coleta, PneusColeta

class ColetaForm(forms.ModelForm):
    class Meta:
        model = Coleta
        fields = ['numero_apanha', 'cliente', 'vendedor', 'forma_pagamento']
        widgets = {
            'numero_apanha': forms.TextInput(attrs={'class': 'form-input'}),
            'cliente': forms.Select(attrs={'class': 'form-select'}),
            'vendedor': forms.Select(attrs={'class': 'form-select'}),
            'forma_pagamento': forms.Select(attrs={'class': 'form-select'}),
        }

class PneusColetaForm(forms.ModelForm):
    class Meta:
        model = PneusColeta
        fields = ['serie', 'fogo', 'tamanho', 'desenho', 'fabricante', 'valor', 'montado', 'observacao', 'garantia']
        widgets = {
            'serie': forms.TextInput(attrs={'class': 'form-input'}),
            'fogo': forms.TextInput(attrs={'class': 'form-input'}),
            'tamanho': forms.Select(attrs={'class': 'form-select'}),
            'desenho': forms.Select(attrs={'class': 'form-select'}),
            'fabricante': forms.TextInput(attrs={'class': 'form-input'}),
            'valor': forms.NumberInput(attrs={'class': 'form-input', 'step': '0.01'}),
            'garantia': forms.CheckboxInput(attrs={'class': 'form-checkbox'}),
            'montado': forms.CheckboxInput(attrs={'class': 'form-checkbox'}),
            'observacao': forms.Textarea(attrs={'class': 'form-textarea'}),
        }

PneusColetaFormSet = forms.inlineformset_factory(
    Coleta, 
    PneusColeta,
    form=PneusColetaForm,
    extra=1,
    can_delete=True,
    max_num=50  # Aumentando o número máximo de formulários
)
