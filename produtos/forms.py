from django import forms
from .models import Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['descricao', 'preco', 'quantidade', 'peso','voltagem','marca','tipo']
