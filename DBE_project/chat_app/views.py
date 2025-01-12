from chat_app.models import Message, Group
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.core.paginator import Paginator


def index(request):
    return render(request, 'chat/index.html')

def index_view(request):
    
    return render(request, 'chat/index.html')

def chatroom_view(request):
    
    return render(request, 'chat/chatroom.html')

def login_view(request):
    
    return render(request, 'registration/login.html')

def register_view(request):
    
    return render(request, 'registration/register.html')

"""

def chat_room(request, group_id):
    group = get_object_or_404(Group, id=group_id) 
    messages = Message.objects.filter(group=group).order_by('timestamp')  
    
    return render(request, 'chat_room.html', {
        'group': group,
        'messages': messages,
    })
"""

"""
def chatroom(request, group_id):
    group = Group.objects.get(id=group_id)
    messages = Message.objects.filter(group=group).order_by('timestamp')
    return render(request, 'chat/chatroom.html', {'group': group, 'messages': messages})
"""

def chatroom(request, group_id):
    if not group_id:  
        return render(request, 'chat/aucun_groupe.html')
    
    group = get_object_or_404(Group, id=group_id)
    messages = Message.objects.filter(group=group).order_by('timestamp')

    groups = Group.objects.all()
    friends = Friend.objects.all()

    
    friend_paginator = Paginator(friends, 10)  # Affiche 10 amis par page
    page_number = request.GET.get('page')
    friends_page = friend_paginator.get_page(page_number)

    return render(request, 'chat/chatroom.html', {
        'group': group,
        'messages': messages,
        'groups': groups,
        'friends': friends_page,  
        'user': request.user,
    })

"""
def creer_groupe(request):
    if request.method == 'POST':
        group_name = request.POST.get('group_name')
        description = request.POST.get('description')

        # Crée un nouveau groupe avec le nom et la description
        new_group = Group.objects.create(name=group_name, description=description)
        
        # Redirige l'utilisateur ou affiche un message de succès
        return redirect('chatroom')  # Changez 'chatroom' par le nom de votre page principale

    return render(request, 'chat/creer_groupe.html')
"""

def creer_groupe(request):
    if request.method == 'POST':
        name = request.POST.get('group_name')
        description = request.POST.get('description')
        Group.objects.create(name=name, description=description)
        return redirect('chatroom')  # Redirige vers le chatroom  après création
    return render(request, 'chat/creer_groupe.html')

"""

def ajouter_ami(request):
    if request.method == 'POST':
        # Logique pour ajouter un ami
        friend_name = request.POST.get('friend_name')
        # la logique pour sauvegarder l'ami ici
        return render(request, 'chat/ajouter_ami.html', {'success': True})
    return render(request, 'chat/ajouter_ami.html')
"""

def ajouter_ami(request):
    if request.method == 'POST':
        name = request.POST.get('friend_name')
        Friend.objects.create(name=name)
        return redirect('chatroom')  # Redirige vers le chatroom  après ajout
    return render(request, 'chat/ajouter_ami.html')


def group_list(request):
    groups = Group.objects.all()
    return render(request, 'chat/group_list.html', {'groups': groups})



def friend_list(request):
    friends = Friend.objects.all()
    return render(request, 'chat/friend_list.html', {'friends': friends})




def aucun_groupe(request):
    return render(request, 'chat/aucun_groupe.html')




def emoji_picker(request):
   
    emojis_by_category = {}
    emojis = Emoji.objects.all()

   
    for emoji in emojis:
        if emoji.category not in emojis_by_category:
            emojis_by_category[emoji.category] = []
        emojis_by_category[emoji.category].append(emoji)

    return render(request, 'chat/emoji_picker.html', {'emojis_by_category': emojis_by_category})