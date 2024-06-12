from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Paciente
from django.http import HttpResponseNotAllowed

@login_required(redirect_field_name='login')

def home(request):
    # User.objects.create_user(username='caio', email='caio@gmail.com', password='123123')
    return render(request, 'home.html')


def cadastrar_paciente(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        peso = request.POST.get('peso')
        altura = request.POST.get('altura')
        nutricionista = request.user
        novo_paciente = User.objects.create_user(username=nome, email=email, password=senha)
        paciente = Paciente.objects.create(user=novo_paciente, nutricionista=nutricionista, peso=peso, altura=altura)
        return redirect('home')  
    return render(request, 'novo-paciente.html')  

def pacientes(request):
    nutricionista = request.user
    pacientes = Paciente.objects.filter(nutricionista=nutricionista)
    return render(request, 'pacientes.html', {'pacientes': pacientes})


def editar_paciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, pk=paciente_id)
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        peso = request.POST.get('peso')
        altura = request.POST.get('altura')

        paciente.user.username = nome
        paciente.user.email = email
        paciente.user.save()
        paciente.peso = peso
        paciente.altura = altura
        paciente.save()

        return redirect('pacientes')  

    return render(request, 'editar-paciente.html', {'paciente': paciente})
