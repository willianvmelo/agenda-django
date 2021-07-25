from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.http import Http404
from .models import Contato

def index(request):
    #### Recupera dados do banco e armazena na variável. Filtra e só exibe os contatos marcados como True ###
    contatos = Contato.objects.order_by('-id').filter(
        mostrar = True
    ) 

    paginator = Paginator(contatos,20)
    page = request.GET.get('p')

    contatos = paginator.get_page(page)
    return render(request,'contatos/index.html',{
        'contatos':contatos
    })
def ver_contato(request, contato_id):
    
    # contato = Contato.objects.get(id = contato_id) --> Recupera dados do banco e armazena na variável
    contato = get_object_or_404(Contato,id = contato_id) # Trata erros como 404 se o contato não existir.
    # 404 quando o contato estiver marcado como não mostrar.

    if not contato.mostrar:
        raise Http404()
    return render(request,'contatos/ver_contato.html',{
        'contato':contato
    })

def busca(request):
    # Obtém o termo pesquisado através da url.
    termo = request.GET.get('termo')
    contatos = Contato.objects.order_by('-id').filter(
        nome__icontains = termo,
        mostrar = True
    ) 

    paginator = Paginator(contatos,20)
    page = request.GET.get('p')

    contatos = paginator.get_page(page)
    return render(request,'contatos/busca.html',{
        'contatos':contatos
    })