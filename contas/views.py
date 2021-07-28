# Imports
from django.shortcuts import redirect, render
from django.contrib import messages,auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def login(request):
    if request.method != 'POST':
        return render(request, 'contas/login.html')

    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')    
    
    user = auth.authenticate(request, username = usuario, password = senha)

    if not user :
        messages.error(request, 'Usuário ou senha inválidos!')
        return render(request, 'contas/login.html')
    else :
        auth.login(request, user )    
        messages.success(request, 'Logado com sucesso!')
        return redirect('dashboard')
def logout(request):
    auth.logout(request)
    return redirect('index')


def cadastro(request):
    if request.method != 'POST':
        return render(request, 'contas/cadastro.html')
    

    # Obtendo variáveis

    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    email = request.POST.get('email')
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')
    senha2 = request.POST.get('senha2')

    # Verifica se existe algum campo vazio

    if not nome or not sobrenome or not email or not usuario or not senha or not senha or not senha2:
        messages.error(request, 'Nenhum campo pode estar vazio!')
        return render(request, 'contas/cadastro.html')

    # Valida o e-mail
     
    try:
        validate_email(email)
    except:
        messages.error(request, 'Email inválido!')
        return render(request, 'contas/cadastro.html')

    if User.objects.filter(email = email).exists():
        messages.error(request, 'Email já existe.')
        return render(request, 'contas/cadastro.html')    

# Valida o senha
     
    if len(senha) < 6:
        messages.error(request, 'Senha precisa ter  6 caracteres ou mais.')
        return render(request, 'contas/cadastro.html')
    if senha != senha2:
        messages.error(request, 'Senhas não conferem.')
        return render(request, 'contas/cadastro.html')

# Valida o Usuario
     
    if len(usuario) < 6:
        messages.error(request, 'Usuario precisa ter  6 caracteres ou mais.')
        return render(request, 'contas/cadastro.html')

    if User.objects.filter(username = usuario).exists():
        messages.error(request, 'Usuario já existe.')
        return render(request, 'contas/cadastro.html')


    messages.success(request, 'Usuário registrado com sucesso!')
    user = User.objects.create_user (username = usuario, email = email, password = senha, 
    first_name = nome, last_name = sobrenome)
    user.save()

    return redirect('login')  

@login_required(redirect_field_name='login')
def dashboard(request):
    return render(request, 'contas/dashboard.html')    
