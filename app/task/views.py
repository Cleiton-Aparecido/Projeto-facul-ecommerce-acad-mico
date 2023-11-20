from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required



# Create your views here.

# Home do Projeto

def home(request):
    return render(request,'home/home.html')


def sigup(request):

    if request.method == 'GET':

        return render(request,'sigup.html', {
            'form' : UserCreationForm
        } )   

    else: 
        if request.POST['password1'] == request.POST['password2']:

            try: 
                
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                
                login(request, user)
               
                return redirect('tasks')
                
            except:
                return render (request,'sigup.html', { 
                    'form' : UserCreationForm ,
                    "error": 'Usuário já existe'
                    
                    } ) 
           
        return render (request,'sigup.html', { 
                    'form' : UserCreationForm ,
                    "error": 'senhas são diferentes'
                    
                    } ) 

def sigin(request):

    if request.method == 'GET':
        return render(request,'sigin.html', {
        'form': AuthenticationForm
        })

    else:
        user = authenticate(

            request, username=request.POST['username'], password=request.POST['password'])

        if user is None:
            return render(request, 'sigin.html', {
                    'form' : AuthenticationForm,
                    'error': 'Usuário ou senha está incorreto'
                })

        else:
                login(request, user)
                return redirect('tasks')    


@login_required   
def sair(request):
    logout (request)
    return redirect('home')

def tasks(request):
    return render(request,'home/home.html')


@login_required
def venda(request):
    # return render(request,'vendas/index.html')
    return render(request,'home/home.html')


@login_required
def publicar_item_venda(request):
    if request.method == 'POST':
        # Obter dados do formulário
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        valor_str = request.POST.get('valor')
        quantidade = request.POST.get('quantidade')

        # Validar e converter o valor para um número decimal (float)
        try:
            valor = float(valor_str.replace(',', '.'))  # Substituir vírgula por ponto para lidar com valores formatados
        except ValueError:
            # Tratar erro de conversão
            # Você pode retornar uma resposta de erro ou lidar de acordo com a sua lógica de validação
            return render(request, 'erro.html', {'mensagem': 'Valor inválido'})

        # Obter o usuário atualmente autenticado
        usuario = request.user


        # Criar um novo objeto Item e salvar no banco de dados
        novo_item = Itens(nome=nome, descricao=descricao, valor=valor, quantidade=quantidade)
        novo_item.save()

        # Criar um novo objeto Venda e vincular ao usuário e ao item recém-criado
        nova_venda = Vendas(quantidade=0, usuario=usuario, item=novo_item)
        nova_venda.save()

        # Redirecionar para a página desejada após a publicação bem-sucedida
        # Neste exemplo, estou redirecionando para a página inicial ('home')
        return redirect('home')

    # Se o método não for POST, renderizar a página inicial
    return render(request, 'home/home.html')

