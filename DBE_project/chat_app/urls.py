from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('chat/', views.chatroom, name='chatroom_default'),
    path('chat/<int:group_id>/', views.chat_room, name='chat_room'),
    path('creer-groupe/', views.creer_groupe, name='creer_groupe'),
    path('ajouter-ami/', views.ajouter_ami, name='ajouter_ami'),
    path('chatroom/', views.chatroom, name='chatroom'),

    path('chatroom/<int:group_id>/', views.chatroom, name='chatroom'),
    path('creer-groupe/', views.creer_groupe, name='creer_groupe'),
    path('friend-list/', views.friend_list, name='friend_list'),
    path('group-list/', views.group_list, name='group_list'),
    path('ajouter-ami/', views.ajouter_ami, name='ajouter_ami'),


    path('aucun-groupe/', views.aucun_groupe, name='aucun_groupe'),
    path('emoji-picker/', views.emoji_picker, name='emoji_picker'),
    

]
