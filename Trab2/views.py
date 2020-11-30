from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse

def homeSec(request):
    return render(request, "registro/homeSec.html")

def registro(request):
    if request.method == 'POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('sec-home')
        else:
            context = {'form' : formulario, }
            return render(request, 'registro/registro.html', context)
    else:
        formulario = UserCreationForm()
        context = {'form' : formulario, }
        return render(request, 'registro/registro.html', context)


def verificaUsername(request):
        username = request.GET.get('username', None)
        existe = User.objects.filter(username__iexact=username).exists()
        resposta = {
            'existe' : existe,
        }
        return JsonResponse(resposta)

def verificaPassword(request):
    password = request.GET.get('password', None)

    valido = len(password) >= 8 and not password.isdigit()
    resposta = {
        'valido': valido
    }

    return JsonResponse(resposta)

def verificaPasswordConfirmation(request):
    password = request.GET.get('password', None)
    passwordConfirmation = request.GET.get('passwordConfirmation', None)

    same = password == passwordConfirmation
    resposta = {
        'same': same
    }

    return JsonResponse(resposta)