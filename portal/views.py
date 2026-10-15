from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return render(
        request,

        # ERRO ENCONTRADO: O caminho para o arquivo index.html está incorreto.
        # CORREÇÃO: Alterar o caminho para 'portal/index.html'. Essa é a opção correta, pois quando o render() é utilizado o Django já sabe que deve inciar a procura pelo arquivo na pasta templates.
        # 'templates/portal/index.html'
        'portal/index.html'
    )

def cadastro(request):
    return HttpResponse('Página de Cadastro')