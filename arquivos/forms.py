from django import forms
from arquivos.models import Arquivo
from arquivos.models import Texto
from django.forms import ClearableFileInput

# Formulário para inserir um arquivo (no banco de dados)
class ArquivoModel2Form(forms.ModelForm):
    class Meta:
        # usando o modelo Pessoa
        model = Arquivo
        # criar um formulário usando TODOS os campos
        fields = ['arquivo']
        widgets = {
            'arquivo': ClearableFileInput(attrs={'multiple': True}, ),
        }

class TextoModel2Form(forms.ModelForm):
    class Meta:
        # usando o modelo Pessoa
        model = Texto
        # criar um formulário usando TODOS os campos
        fields = ['titulo']


