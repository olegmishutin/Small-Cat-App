import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.exceptions import DenyConnection
from asgiref.sync import sync_to_async
from .models import Message
from .serializers import MessageSerializer


@sync_to_async
def get_dict_of_messages():
    messages = Message.objects.all().select_related('sender')
    messages_serializer = MessageSerializer(messages, many=True)
    return messages_serializer.data


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = 'general_chat'

        if not self.scope['user'].is_authenticated:
            raise DenyConnection('Не аутентифицированный пользователь')

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

        messages_data = await get_dict_of_messages()

        await self.send(text_data=json.dumps(
            messages_data, ensure_ascii=False
        ))

    async def receive(self, text_data=None, bytes_data=None):
        message = json.loads(text_data).get('message').strip()

        if message:
            await Message.objects.acreate(sender=self.scope['user'], text=message)

            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'text': message,
                    'sender': self.scope['user'].username
                }
            )

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def chat_message(self, event):
        await self.send(text_data=json.dumps({
            'text': event['text'],
            'sender': event['sender']
        }, ensure_ascii=False))
