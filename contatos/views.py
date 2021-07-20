from django.shortcuts import render
from .models import Contato

def index(request):
    contatos = Contato.objects.all() #Recupera dados do banco e armazena na variável
    return render(request,'contatos/index.html',{
        'contatos':contatos
    })
def ver_contato(request, contato_id):
    contato = Contato.objects.get(id = contato_id) #Recupera dados do banco e armazena na variável
    return render(request,'contatos/ver_contato.html',{
        'contato':contato
    })