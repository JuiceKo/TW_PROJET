from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.chatroom_list, name='chatroom_list'),
    path('create/', views.create_chatroom, name='create_chatroom'),
    path('<int:room_id>/', views.chatroom_detail, name='chatroom_detail'),
]
