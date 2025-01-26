from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.chatroom_list, name='chatroom_list'),
    path('create/', views.create_channel_view, name='create_chatroom'),
    path('<int:room_id>/', views.chatroom_detail, name='chatroom_detail'),
    path('channel/<int:room_id>/delete/', views.delete_channel, name='delete_channel'),
    path('my-channels/', views.user_channels, name='user_channels'),
]
