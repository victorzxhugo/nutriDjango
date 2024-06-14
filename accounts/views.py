from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User

def login(request):
    if request.method == "POST":
        usuario = request.POST['username']
        senha = request.POST['password']

        verificarUsuario = auth.authenticate(request, username=usuario, password=senha)
        if verificarUsuario != None:
            auth.login(request, verificarUsuario)
            print(verificarUsuario)

            return redirect('home')    
        else:
            print(verificarUsuario)   
    return render(request, 'pages/login.html')

def register(request):
    if request.method == "POST":
        usuario = request.POST['username']
        email = request.POST['email']
        senha = request.POST['password']
        repita_sua_senha = request.POST['repeatPassword']

        User.objects.create_user(
            username=usuario,
            email=email,
            password=senha)
        return redirect('login')
    return render(request, 'pages/register.html')


def logout(request):
    auth.logout(request)
    return redirect('login')