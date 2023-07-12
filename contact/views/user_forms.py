from django.shortcuts import render, redirect
from django.contrib import messages
from contact.forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth

def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário registrado')
            return redirect('contact:login')

    return render(
        request, 
        'contact/register.html',
        {
            'form':form
        }
    )

def login_view(request):
    form = AuthenticationForm(request)

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

    if form.is_valid():
        #pega o usuario
        user = form.get_user()
        #loga o usuario
        auth.login(request, user)
        messages.success(request, 'Logado com sucesso')
        return redirect('contact:index')

    return render(
        request, 
        'contact/login.html',
        {
            'form':form
        }
    )

def logout_view(request):
    auth.logout(request)
    return redirect('contact:login')