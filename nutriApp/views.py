from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# @login_required(redirect_field_name='login')

def home(request):
    # User.objects.create_user(username='caio', email='caio@gmail.com', password='123123')
    if request.user.id != None:
        return render(request, 'portal/home.html')
    else:
        return redirect('login')
