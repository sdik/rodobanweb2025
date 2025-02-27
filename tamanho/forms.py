from django import forms
from .models import Tamanho

class TamanhoForm(forms.ModelForm):
    class Meta:
        model = Tamanho
        fields = ['medida', 'status']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-1 focus:ring-blue-500' 