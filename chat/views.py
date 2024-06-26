from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages  
from .forms import SignUpForm, GroupForm
from .models import Group, Message

def index(request):
    welcome_message = f"Hi {request.user.username}," if request.user.is_authenticated else None
    return render(request, 'chat/index.html', {'welcome_message': welcome_message})

@login_required
def groups(request):
    groups = Group.objects.all()
    return render(request, 'chat/group_list.html', {'groups': groups})

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

def group_list(request):
    groups = Group.objects.all()
    context = {
        'groups': groups
    }
    return render(request, 'chat/group_list.html', context)

def group_create(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('group_list')
    else:
        form = GroupForm()
    return render(request, 'chat/group_form.html', {'form': form})

def group_update(request, pk):
    group = get_object_or_404(Group, pk=pk)
    if request.method == 'POST':
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return redirect('group_list')
    else:
        form = GroupForm(instance=group)
    return render(request, 'chat/group_form.html', {'form': form})

def group_chat(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    messages = group.messages.all().order_by('timestamp')
    return render(request, 'chat/group_chat.html', {'group': group, 'messages': messages})

def send_message(user, content):
    message = Message.objects.create(user=user, content=content)
    return message

def get_messages():
    messages = Message.objects.all()
    return messages
