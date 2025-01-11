from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from .models import Channel, Message
from .forms import CustomUserCreationForm



def landing_page(request):
    if request.user.is_authenticated:
        return redirect('chatroom_list')
    return render(request, 'chat_app/landing_page.html')


def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('chatroom_list')
    else:
        form = CustomUserCreationForm()

    return render(request, 'chat_app/register.html', {'form': form})


@login_required
def chatroom_list(request):
    rooms = Channel.objects.all()
    return render(request, 'chat_app/chatroom_list.html', {'rooms': rooms})

@login_required
def chatroom_detail(request, room_id):
    room = get_object_or_404(Channel, id=room_id)
    messages = room.messages.order_by('timestamp')

    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Message.objects.create(chatroom=room, user=request.user, content=content)
        return redirect('chatroom_detail', room_id=room.id)

    return render(request, 'chat_app/chatroom_detail.html', {'room': room, 'messages': messages})

@login_required
def create_chatroom(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            Channel.objects.create(name=name)
        return redirect('chatroom_list')
    return render(request, 'chat_app/create_chatroom.html')

@login_required
def join_chatroom(request, room_id):
    room = get_object_or_404(Channel, id=room_id)
    if request.user not in room.members.all():
        room.members.add(request.user)
        Message.success(request, f'Vous avez rejoint le salon {room.name} avec succès!')
    else:
        Message.info(request, f'Vous êtes déjà membre du salon {room.name}.')
    return redirect('chatroom_detail', room_id=room.id)

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            Message.success(request, 'Connexion réussie!')
            return redirect('chatroom_list')
        else:
            Message.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')

    return render(request, 'chat_app/login.html')