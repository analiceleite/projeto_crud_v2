from django import forms
from .models import Funcionario

class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ['nome', 'edv', 'cargo', 'setor','endereco','horario_entrada','horario_saida','data_admissao']