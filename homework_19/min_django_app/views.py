from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegistrationForm, LoginForm
from .models import User

def register_view(request):
    '''Обрабатывает регистрацию пользователей.'''

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful. Please log in.")
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'min_django_app/register.html', {'form': form})

def login_view(request):
    '''Обрабатывает вход пользователя.'''

    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(email=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, "Invalid credentials")
    else:
        form = LoginForm()
    return render(request, 'min_django_app/login.html', {'form': form})

def logout_view(request):
    '''Обрабатывает выход пользователя.'''

    logout(request)
    return redirect('login')

def trigger_error(request):
    '''Для тестирования.'''
    raise Exception("Test 500 error")

