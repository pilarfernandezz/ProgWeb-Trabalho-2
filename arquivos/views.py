from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse_lazy
from django.shortcuts import get_object_or_404

from arquivos.forms import ArquivoModel2Form
from arquivos.forms import TextoModel2Form

from arquivos.models import Arquivo
from arquivos.models import Texto
import datetime

class ArquivoDeleteView(View):
    def get(self, request, pk, *args, **kwargs):
        texto = Texto.objects.get(pk=pk)
        context = {'texto': texto,}
        return render(request, 'arquivos/apagaArquivo.html' , context)

    def post(self, request, pk, *args, **kwargs):
        texto = Texto.objects.get(pk=pk)
        texto.delete()
        return HttpResponseRedirect(reverse_lazy('arquivos:lista-arquivo'))

class ArquivoUpdateView(View):
    def get(self, request, pk, *args, **kwargs):
        texto = Texto.objects.get(pk=pk)
        formulario = TextoModel2Form(instance=texto)
        context = {'formulario' : formulario,}
        return render(request, 'arquivos/atualizaArquivo.html', context)

    def post(self, request, pk, *args, **kwargs):
        texto = get_object_or_404(Texto, pk=pk)
        formulario = TextoModel2Form(request.POST, instance=texto)
        if formulario.is_valid():
            texto = formulario.save()
            texto.save()
            return HttpResponseRedirect(reverse_lazy('arquivos:lista-arquivo'))
        else:
            context = {'formulario' : formulario,}
            return render(request, 'arquivos/atualizaArquivo.html', context)


class ArquivoListView(View):
    def get(self, request, *args, **kwargs):
        textos = Texto.objects.all()
        context = {
            'textos': textos,
        }

        return render(request, 'arquivos/listaArquivos.html', context)

class ArquivoCreateView(View):
    def get(self, request, *args, **kwargs):
        context = { 'form_texto': TextoModel2Form, 'form_arquivo': ArquivoModel2Form}
        return render(request, 'arquivos/criaArquivos.html', context)


    def post(self, request, *args, **kwargs):
        form_arquivo = ArquivoModel2Form(request.POST, request.FILES)
        form_texto = TextoModel2Form(request.POST)
        
        files = request.FILES.getlist('arquivo')

        content = ""
        for file in files:
            content += file.read().decode("utf-8")
            content += ' '

        if  form_texto.is_valid():  
            arquivo = form_texto.save(commit=False)
            arquivo.conteudo = content
            arquivo.data = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            arquivo.save()
            return HttpResponseRedirect(reverse_lazy('arquivos:lista-arquivo'))
        else:
            return HttpResponseRedirect(reverse_lazy('arquivos:cria-arquivo'))
