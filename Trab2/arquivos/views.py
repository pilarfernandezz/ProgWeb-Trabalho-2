from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse_lazy
from arquivos.forms import ArquivoModel2Form
from arquivos.models import Arquivo

# Create your views here.
class ArquivoDeleteView(View):
    def a(): return

class ArquivoUpdateView(View):
    def a(): return

class ArquivoListView(View):
    def get(self, request, *args, **kwargs):
        arquivos = Arquivo.objects.all()
        print(arquivos)
        context = {
            'arquivos': arquivos,
        }

        return render(request, 'arquivos/listaArquivos.html', context)




class ArquivoCreateView(View):
    def get(self, request, *args, **kwargs):
        context = {'formulario' : ArquivoModel2Form}
        return render(request, 'arquivos/criaArquivos.html', context)

    # Cria um arquivo com os dados do formulário no banco de dados
    def post(self, request, *args, **kwargs):
        # formulário representa os dados do formulário vindos via POST
        formulario = ArquivoModel2Form(request.POST, request.FILES)

        print("aaaaa"+str(formulario))
        if formulario.is_valid():
            # criar uma variável que representa o contato
            arquivo = formulario.save()
        
                # o contato ainda está somente em memória
                # vou salvar no banco de dados
            arquivo.save()
                # eu NÃO vou desviar para um template e sim para outro view
                # vai desviar para a URL lista-contato definida em contatos
            return HttpResponseRedirect(reverse_lazy('arquivos:lista-arquivo'))
        else:
            print("-----------------------------")
            return HttpResponseRedirect(reverse_lazy('arquivos:cria-arquivo'))
