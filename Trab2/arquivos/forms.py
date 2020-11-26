from django import forms
from arquivos.models import Arquivo

# Formulário para inserir um arquivo (no banco de dados)
class ArquivoModel2Form(forms.ModelForm):
    class Meta:
        # usando o modelo Pessoa
        model = Arquivo
        # criar um formulário usando TODOS os campos
        fields = '__all__'
