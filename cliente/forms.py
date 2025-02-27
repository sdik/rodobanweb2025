from django import forms
from .models import Cliente
import re

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date'}),
            'cep': forms.TextInput(attrs={'class': 'mask-cep'}),
            'cpf': forms.TextInput(attrs={'class': 'mask-cpf'}),
            'cnpj': forms.TextInput(attrs={'class': 'mask-cnpj'}),
            'telefone': forms.TextInput(attrs={'class': 'mask-telefone'}),
            'celular': forms.TextInput(attrs={'class': 'mask-celular'}),
        }

    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        if cpf:
            cpf = re.sub(r'[^0-9]', '', cpf)
            if len(cpf) != 11:
                raise forms.ValidationError('CPF deve conter 11 dígitos.')
        return cpf

    def clean_cnpj(self):
        cnpj = self.cleaned_data.get('cnpj')
        if cnpj:
            cnpj = re.sub(r'[^0-9]', '', cnpj)
            if len(cnpj) != 14:
                raise forms.ValidationError('CNPJ deve conter 14 dígitos.')
        return cnpj

    def clean_cep(self):
        cep = self.cleaned_data.get('cep')
        if cep:
            cep = re.sub(r'[^0-9]', '', cep)
            if len(cep) != 8:
                raise forms.ValidationError('CEP deve conter 8 dígitos.')
        return cep

    def clean_telefone(self):
        telefone = self.cleaned_data.get('telefone')
        if telefone:
            telefone = re.sub(r'[^0-9]', '', telefone)
            if len(telefone) not in [10, 11]:
                raise forms.ValidationError('Telefone deve conter 10 ou 11 dígitos.')
        return telefone

    def clean_celular(self):
        celular = self.cleaned_data.get('celular')
        if celular:
            celular = re.sub(r'[^0-9]', '', celular)
            if len(celular) != 11:
                raise forms.ValidationError('Celular deve conter 11 dígitos.')
        return celular

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control' 