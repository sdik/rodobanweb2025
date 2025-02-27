from django import forms
from .models import Vendedor

class VendedorForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = Vendedor
        fields = ['nome', 'apelido', 'telefone', 'senha', 'email', 'percentual_comissao']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-1 focus:ring-blue-500' 