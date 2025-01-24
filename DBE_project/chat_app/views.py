from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from .models import Channel, Message
from .forms import CustomUserCreationForm
from django.contrib import messages




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
    messages = Message.objects.filter(channel=room).order_by('timestamp')
    return render(request, 'chat_app/chatroom_detail.html', {
        'room': room,
        'messages': messages
    })


@login_required
def create_channel_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description', '')

        if name:
            Channel.objects.create(name=name, description=description)
            return redirect('chatroom_list')
        else:
            pass

    return render(request, 'chat_app/create_chatroom.html')

@login_required
def delete_channel(request, room_id):
    channel = get_object_or_404(Channel, id=room_id)
    if request.method == 'POST':
        channel.delete()
        return redirect('chatroom_list')
    return redirect('chatroom_detail', room_id=channel.id)

@login_required
def custom_logout(request):
    if request.method == "POST":
        logout(request)
        return redirect('landing_page')
    return redirect('landing_page')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Connexion réussie!')
            return redirect('chatroom_list')
        else:
            messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')

    return render(request, 'chat_app/login.html')
