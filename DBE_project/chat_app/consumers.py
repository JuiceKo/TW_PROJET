import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from django.utils import timezone

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_id = self.scope['url_route']['kwargs']['room_id']
        self.room_group_name = f'chat_{self.room_id}'
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message_content = data.get('message', '')
        username = data.get('username', '')

        await self.save_message_in_db(username, message_content)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message_content,
                'username': username
            }
        )

    async def chat_message(self, event):
        message = event['message']
        username = event['username']
        await self.send(text_data=json.dumps({
            'message': message,
            'username': username
        }))

    @database_sync_to_async
    def save_message_in_db(self, username, message_content):
        from django.contrib.auth.models import User
        from .models import Channel, Message

        try:
            channel_obj = Channel.objects.get(id=self.room_id)
            user_obj = User.objects.get(username=username)
        except (Channel.DoesNotExist, User.DoesNotExist):
            return

        Message.objects.create(
            channel=channel_obj,
            user=user_obj,
            content=message_content,
            timestamp=timezone.now()
        )
