from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Paciente
from django.http import HttpResponseNotAllowed
from django.core.exceptions import ValidationError

@login_required(redirect_field_name='login')
def home(request):
    # User.objects.create_user(username='caio', email='caio@gmail.com', password='123123')
    return render(request, 'home.html')

@login_required(redirect_field_name='login')
def cadastrar_paciente(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        nome_completo = request.POST.get('nome_completo')
        genero = request.POST.get('genero')
        data_nascimento = request.POST.get('data_nascimento')
        ocupacao = request.POST.get('ocupacao')
        cep = request.POST.get('cep')
        celular = request.POST.get('celular')
        print(username)
        try:
            novo_usuario = User.objects.create_user(username=username, email=email, password=senha)
            Paciente.objects.create(
                user=novo_usuario,
                nutricionista=request.user,
                nome_completo=nome_completo,
                genero=genero,
                data_nascimento=data_nascimento,
                ocupacao=ocupacao,
                cep=cep,
                celular=celular
            )
            return redirect('home')
        except ValidationError as e:
            print(f"Error: {e}")
            return render(request, 'novo-paciente.html', {'errors': e})

    return render(request, 'novo-paciente.html')

@login_required(redirect_field_name='login')
def pacientes(request):
    nutricionista = request.user
    pacientes = Paciente.objects.filter(nutricionista=nutricionista)
    return render(request, 'pacientes.html', {'pacientes': pacientes})


@login_required(redirect_field_name='login')
def editar_paciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, pk=paciente_id)
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        peso = request.POST.get('peso')
        data_nascimento = request.POST.get('data_nascimento')
        genero = request.POST.get('genero')


        paciente.user.save()
        paciente.peso = peso
        paciente.data_nascimento = data_nascimento
        paciente.genero = genero
        paciente.save()

        return redirect('pacientes') 

    return render(request, 'editar-paciente.html', {'paciente': paciente})
