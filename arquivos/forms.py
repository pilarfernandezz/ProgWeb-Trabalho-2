from django import forms
from arquivos.models import Arquivo
from arquivos.models import Texto
from django.forms import ClearableFileInput

# Formulário para inserir um arquivo (no banco de dados)
class ArquivoModel2Form(forms.ModelForm):
    class Meta:
        model = Arquivo
        fields = ['arquivo']
        widgets = {
            'arquivo': ClearableFileInput(attrs={'multiple': True}, ),
        }

# Formulário que guarda o conteúdo do arquivo
class TextoModel2Form(forms.ModelForm):
    class Meta:
        model = Texto
        fields = ['titulo']


