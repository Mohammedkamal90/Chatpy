from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm

def index(request):
    return render(request, 'chat/index.html')

@login_required
def chat_view(request):
    return render(request, 'chat/chat.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        auth_logout(request)
        return redirect('index')
    return render(request, 'registration/logout.html')

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'registration/register.html', {'form': form})