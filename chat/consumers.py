import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Message, Group
from django.contrib.auth.models import User

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_id = self.scope['url_route']['kwargs']['group_id']
        self.group_name = f'chat_{self.group_id}'

        # Join group
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave group
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        user = self.scope['user']
        group = await Group.objects.get(pk=self.group_id)

        # Save message to database
        await Message.objects.create(user=user, group=group, content=message)

        # Broadcast message to group
        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'chat_message',
                'message': message,
                'user': user.username,
            }
        )

    async def chat_message(self, event):
        message = event['message']
        user = event['user']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'user': user,
        }))
